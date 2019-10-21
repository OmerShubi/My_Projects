%% Initializing Parameters
t = 0.1;
x0 = [10; -1];
eps = 10^-5;

%% Creating Functions
proj = Domain();
f = @(x) x(1)^2-2*x(2)+log(exp(x(1))+exp(x(2)));
gf = @(x) [2*x(1) + exp(x(1))/(exp(x(1))+exp(x(2)));...
            -2 + exp(x(2))/(exp(x(1))+exp(x(2)))];

%% Projection Gradient Descent Algorithm
[x, fs] = Projection_Gradient_Descent_Algorithm(f, gf, proj, t, x0, eps);

%%Plotting Results
plot(fs)
x
