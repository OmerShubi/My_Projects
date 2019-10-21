function [x , x_noise, fs, fs_noise] = grad_noise(f , g_x, g_y , t_k , x0 , mu, sigma, eps)

% Input checks
if ~isa(f,'function_handle') || ~isa(g_x,'function_handle') || ~isa(g_y,'function_handle')
	error("f, g_x, g_y and lsearch  must be functions")
end
if eps<=0 || ~isreal(eps) || ~isscalar(eps)
        error("eps must be a real positive scalar")
end
if  sigma<0 || ~isreal(mu) || ~isreal(sigma)
        error("mu and sigma must be a valid inputs")
end
if ~isreal(x0)
    error("x0 must be real")
end

% Initialize Paramaters
x_noise = x0;
grad  = [g_x(x_noise(1,1));g_y(x_noise(2,1))]; 

% Result containers
fs_noise = f(x0)+0.25;

% Execute  Gradient Descent Algorithm
while (abs(f(x_noise)-f(x_noise -(t_k * grad))) > eps)
    b = normrnd(mu, sigma,[2,1]);
    x_noise = x_noise - (t_k * grad)+b;
    grad  = [g_x(x_noise(1,1));g_y(x_noise(2,1))]; 
    
    % Recording interim results
    fs_noise = [fs_noise, (f(x_noise)+0.25)];

end

% Initialize Paramaters
x = x0;
grad  = [g_x(x(1,1));g_y(x(2,1))]; 

% Result containers
fs = f(x)+0.25;

% Execute  Gradient Descent Algorithm
while (abs(f(x)-f(x -(t_k * grad))) > eps)
    x = x - (t_k * grad);
    grad  = [g_x(x(1,1));g_y(x(2,1))]; 
    
    % Recording interim results
    fs = [fs, (f(x)+0.25)];
end

end