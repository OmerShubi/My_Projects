% Initialize Paramaters
A = [14 3 2 2 3;
     3 13 2 2 3;
     2 2 13 2 2;
     2 2 2 12 2;
     3 3 2 2 13];
alpha = 0.5;
beta = 0.5;
s = 1;
x0 = [1 1 1 1 1]';
t_k = 1 / (2*max(eig(A'*A)));
f =@(x) 0.5 * x'*((A')*A)*x;
g =@(x) A'*A*x; % f gradient
eps = 10^-5;

% Run calculations
[x_const, fs_const, gs_const, ts_const] = generic_grad(f, g, const_step(t_k), x0, eps);
[x_exact, fs_exact, gs_exact, ts_exact] = generic_grad(f, g, exact_quad(A), x0, eps);
[x_back, fs_back, gs_back, ts_back] = generic_grad(f, g, back(alpha, beta, s), x0, eps);

% Plot fs versus Number of Iterations
figure('Name','fs vs Iters Comparison');
loglog(fs_exact);
hold on;
loglog(fs_const);
hold on;
loglog(fs_back);
title('Loglog Plot of fs vs  Number of Iterations');
xlabel('Iteration');
ylabel('f(x)');
legend({'fs\_exact\_quad','fs\_const', 'fs\_back'},'Location','southwest');

% Plot gs versus Number of Iterations
figure('Name','gs vs Iters Comparison');
loglog(gs_exact);
hold on;
loglog(gs_const);
hold on;
loglog(gs_back);
title('Loglog Plot of gs vs Number of Iterations');
xlabel('Iteration') ;
ylabel('||\nablaf(x)||_2');
legend({'gs\_exact\_quad','gs\_const','gs\_back'},'Location','southwest');

% Plot gs versus Time
figure('Name', 'gs vs Time Comparison');
semilogy(ts_exact, gs_exact);
hold on;
semilogy(ts_const, gs_const);
hold on;
semilogy(ts_back, gs_back);
title('Semilog Plot of gs vs Time');
xlabel('Time') ;
ylabel('||\nablaf(x)||_2')    ;
legend({'gs\_exact\_quad','gs\_const','gs\_back'},'Location','northeast');