function [x, x_noise, fs, fs_noise] = noisy_gd_initializer(mu, sigma, x0, epsilon)

% Assuming Valid input. Input errors handled by grad_noise function

% Defining specific function handles and parameters for this exercise
f =@(xk) xk(1)^2-xk(2)^2+xk(2)^4;
g_x =@(xk) 2*xk; 
g_y =@(yk) 4*yk^3-2*yk;
t_k = 0.1;

% Execute optimization algorithm
[x, x_noise, fs, fs_noise] = grad_noise(f, g_x, g_y, t_k, x0, mu, sigma, epsilon);

end

