function [x , fs , gs , ts] = generic_grad(f , gf , lsearch , x0 , eps)


% Input checks
if ~isa(f,'function_handle') || ~isa(gf,'function_handle') || ~isa(lsearch,'function_handle')
	error("f, gf and lsearch  must be functions")
end
if eps<=0 || ~isreal(eps) || ~isscalar(eps)
        error("eps must be a real positive scalar")
end
if ~isreal(x0)
    error("x0 must be real")
end
% Start Timer
tic

% Initialize Paramaters
x = x0;
grad = gf(x);
grad_norm = norm(grad);

% Result containers
gs = grad_norm;
fs = f(x0);
ts = 0;
% Execute Generic Gradient Descent Algorithm
while (grad_norm > eps)
    t_k = lsearch(f,x,grad);
    x = x - (t_k * grad);
    grad = gf(x);
    grad_norm = norm(grad);
    
    % Recording interim results
    fs = [fs, f(x)];
    gs = [gs, grad_norm];
    ts = [ts, toc]; 
end
end

