function lsearch = exact_quad(A)

% verify A is Positive Definite
[~,p] = chol(A);
if (p~=0)
    error("A must be a postitive definite matrix")
end

lsearch = @(f,x,g_k) (norm(g_k)^2)/(g_k'*(A')*A*g_k);
end

