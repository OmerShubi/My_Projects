%Initialize parameters according to requirements
mu = 0;
sigma = 0.0005;
x0 = [100;0];
epsilon = 10^-8;

% Execution
[x, x_noise, fs, fs_noise] = noisy_gd_initializer(mu, sigma, x0, epsilon)

% Plot fs versus Number of Iterations
figure('Name','fs vs Iters Comparison');
loglog(fs);
hold on;
loglog(fs_noise);
title('Loglog Plot of fs vs  Number of Iterations');
xlabel('Iteration');
ylabel('f(x)');
legend({'fs','fs\_noise'},'Location','southwest');

