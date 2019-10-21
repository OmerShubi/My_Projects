

cp Alice_book temp_book # Create a copy so to keep origin the same

# Remove punctuation, stop words, trailing spaces, and turns all to lowercase
cat temp_book | tr -d '[:punct:]' | sed 's/[`“‘”"’]// g' | sed -r 's/\b(a|about|above|across|after|afterwards|again|against|all|almost|alone|along|already|also|although|always|am|among|amongst|amoungst|amount|an|and|another|any|anyhow|anyone|anything|anyway|anywhere|are|around|as|at|back|be|became|because|become|becomes|becoming|been|before|beforehand|behind|being|below|beside|besides|between|beyond|bill|both|bottom|but|by|call|can|cannot|cant|co|computer|con|could|couldnt|cry|de|describe|detail|do|done|down|due|during|each|eg|eight|either|eleven|else|elsewhere|empty|enough|etc|even|ever|every|everyone|everything|everywhere|except|few|fifteen|fify|fill|find|fire|first|five|for|former|formerly|forty|found|four|from|front|full|further|get|give|go|had|has|hasnt|have|he|hence|her|here|hereafter|hereby|herein|hereupon|hers|herself|him|himself|his|how|however|hundred|i|ie|if|in|inc|indeed|interest|into|is|it|its|itse|keep|last|latter|latterly|least|less|ltd|made|many|may|me|meanwhile|might|mill|mine|more|moreover|most|mostly|move|much|must|my|myse|name|namely|neither|never|nevertheless|next|nine|no|nobody|none|noone|nor|not|nothing|now|nowhere|of|off|often|on|once|one|only|onto|or|other|others|otherwise|our|ours|ourselves|out|over|own|part|per|perhaps|please|put|rather|re|same|see|seem|seemed|seeming|seems|serious|several|she|should|show|side|since|sincere|six|sixty|so|some|somehow|someone|something|sometime|sometimes|somewhere|still|such|system|take|ten|than|that|the|their|them|themselves|then|thence|there|thereafter|thereby|therefore|therein|thereupon|these|they|thick|thin|third|this|those|though|three|through|throughout|thru|thus|to|together|too|top|toward|towards|twelve|twenty|two|un|under|until|up|upon|us|very|via|was|we|well|were|what|whatever|when|whence|whenever|where|whereafter|whereas|whereby|wherein|whereupon|wherever|whether|which|while|whither|who|whoever|whole|whom|whose|why|will|with|within|without|would|yet|you|your|yours|yourself|yourselves)\b//I g' | 
sed -e 's/^[ \t]*//;s/[ \t]*$//' | sed '/^$/d' | tr -s " " | tr '[:upper:]' '[:lower:]' > temp

mkdir files_d
mv temp temp_book

# Seperates book into chapters named per the chapter number
awk 'BEGIN{RS="chapter ";}{if(NR!=1){print > "files_d/"(NR-1);}}' temp_book

cp temp_book files_d/0  # stors whole book as well as '0'

# Finds the pair of words (regardless of inner order ('hello world' == 'world hello'))
# That appear the most number of times in a line. Per whole file and per each chapter.
# In addition, finds the word that appears the most as the first word in a line.

for k in {0..12}
do
	awk '
	function sorted(a,b){
		    if (a < b) return a " " b;
		    else return b " " a;
	}
	function find_max(array){
		max_count=0;
		for (key in array){
			if(array[key]!=NULL){
				if(max_count < array[key]){
					max_count = array[key];
					best = key;
				}
				if(max_count == array[key]){
					if(key<best){
						best = key;
					}	 
				}
			}
		}
		return best;
	}
	BEGIN{
		max_pair_count=0;
		max_first_word_count=0;
	}
	{
		for(i=1;i<NF;i=i+1){
			word_pairs[sorted($i,$(i+1))]=word_pairs[sorted($i,$(i+1))]+1;
		}
		first_words[$1]=first_words[$1]+1;
	}
	END{
		best_pair = find_max(word_pairs);
		best_first_word = find_max(first_words);
		# Different print function if for book or for chapter
		if(var==0){
			print "Most common pair in the book: " best_pair; 
			print "Most common first word in the book: " best_first_word; 
		}
		if(var!=0){
			print "Most common pair for chapter " var ": " best_pair; 
			print "Most common first word for chapter " var ": " best_first_word; 
		}
	}' var=$k files_d/$k
done

# Calculate the average line length, how many lines are shorter than the average, 
# and the average place of 'Alice' in a line
awk -v CONVFMT=%.1f '
	BEGIN{
		sum_line_len=0;
		shorter_than_avg=0;
		alice_count=0;
		alice_places=0;
	}
	{
	    line_lengths[NR]=NF;
	    sum_line_len=sum_line_len+NF;
		for(i=1;i<=NF;i=i+1){
			if($i=="alice"){
				alice_count=alice_count+1;
				alice_places=alice_places+i;
			}	
		}	

	}END{
		avg_line_len=sum_line_len/NR;
		print "Average line length: " avg_line_len;

		for(line in line_lengths){
			if(line_lengths[line]<avg_line_len){
				shorter_than_avg=shorter_than_avg+1;
			} 
		}
		print "Number of lines shorter than the average: " shorter_than_avg;

		avg_alice_place=alice_places/alice_count;
		print "Average place of Alice in a line: " avg_alice_place;
	}' temp_book

# Delete temp artifacts
rm temp_book
rm -r files_d # comment this if the processed data is required.
