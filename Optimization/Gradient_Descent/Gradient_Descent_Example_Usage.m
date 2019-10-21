% Randomly Create 50 points in R3
S = zeros(50, 3);
for i=1:50
    S(i, 1:2) = [i, i + normrnd(0, 4)];
    S(i, 3) = normrnd(0, 1) + i;
end

% Initialize paramaters
X = [S(:,1:2), ones(50,1)];
y = S(:,3);
t_k = 1 / (2*max(eig(X'*X)));
eps = 10^-10;
x0 = [1 1 1]';
f=@(w) 0.5*(norm(X*w-y)^2);
g=@(w) X'*(X*w-y);

% Execute optimization
w = generic_grad(f, g, const_step(t_k), x0, eps) % Simplified function from q1

%Plotting results
axis equal
scatter3(S(:, 1), S(:, 2), S(:, 3), 'filled', 'red')
hold on
[x,y] = meshgrid(1:2:50);
z = w(1)*x + w(2)*y + w(3);
surf(x, y, z)
alpha 0.4
scatter3(S(:, 1), S(:, 2), S(:, 3), 'filled', 'red')
