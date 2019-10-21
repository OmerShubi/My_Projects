  
%% Question 1, part 1 
Q1 = [ 1 0 0; 0 2 -1; 0 -1 3];
Q2 = [ 4 -4; -4 6];
cvx_begin
    variable x(3)
    minimize max(abs(2*x(1)-3*x(2)), abs(x(2)-x(1)+x(3))) + quad_form(x,Q1)
    subject to
        square_pos(square_pos(square_pos(quad_form(x(1:2),Q2) + 1/100))) + quad_over_lin(x(3), 2*x(1)+3*x(2)) <= 150;
        x(1)+ x(2) >= 1 - x(2)/2;
cvx_end
