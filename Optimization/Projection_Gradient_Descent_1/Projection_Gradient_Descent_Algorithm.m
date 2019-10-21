function [x, fs] = grad_proj(f, gf, proj, t, x0, eps)
%% Projection Gradient Descent Algorithm
%
% Parameters:
%   f - the function
%   gf - the function's gradient
%   proj - function to calculate projection of a vector into a domain
%   t - step size
%   x0 - starting point
%   eps - tolerance
%
% Returns
% x - the final point found
% fs - vector of f(x) results, length equals number of iterations 


%% Creating containers for results
x_k = x0;
fs = f(x0);

%% first iteration 
x = proj(x0 - t*gf(x0));
fs = [fs, f(x)];

%% Projection Gradient Descent Algorithm
while (norm(x-x_k)>eps)
    x_k = x;
    % Projection Gradient Descent Algorithm
    x = proj(x_k - t*gf(x_k));
    
    % Storing interim result
    fs = [fs, f(x)];
end
