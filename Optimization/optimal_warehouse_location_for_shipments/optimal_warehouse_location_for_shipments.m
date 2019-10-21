%% Initialization Script
m = 50; n = 2; outliers_num = 10;
rand('seed', 314);
A=3000*rand(n, m);
A(:, 1:outliers_num) = A(:, 1:outliers_num) + 3000;
p = round(10*rand(m, 1) + 10);
alpha = 0.01; gamma = 1.2; eta1 = 20; eta2 = 30; mu1=2; mu2=5;

%% CVX Model part 1
cvx_begin
    variable x1(2)
    func1 = 0;
    for i = 1:m
        func1 = func1 + alpha*norm(A(:,i)-x1)*p(i);
    end
    func1 = func1*gamma;
    minimize func1
cvx_end
x1

%% CVX Model part 2
cvx_begin
    variable x2(2)
    func2 = 0;
    for i = 1:m
        flight_time = alpha * norm(A(:,i) - x2);
        flight_cost = gamma * flight_time;
        compensation_1 = mu1 * max(flight_time - eta1, 0);
        compensation_2 = (mu2 - mu1) * max(flight_time - eta2, 0);
        func2 = func2 + p(i) * (flight_cost + compensation_1 + compensation_2);
    end
    minimize func2
cvx_end
x2

%% Plotting results

% Create figure
figure1 = figure;

% Create axes
axes1 = axes('Parent',figure1);
hold(axes1,'on');

% Create scatter
scatter(A(1,:),A(2,:),exp(p/4),'DisplayName','Shipments');

% Create scatter
scatter(x1(1),x1(2),100,'filled','DisplayName','Warehouse1','MarkerFaceColor','flat',...
    'MarkerEdgeColor','none',...
    'Marker','pentagram');

% Create scatter
scatter(x2(1),x2(2),100,'filled','DisplayName','Warehouse2','MarkerFaceColor','flat',...
    'MarkerEdgeColor','none',...
    'Marker','pentagram');

% Create ylabel
ylabel('Y Coordinate');

% Create xlabel
xlabel('X Coordinate');

% Create title
title('Shipment locations & Optimal spots for Warehouse');

% Create legend
legend1 = legend(axes1,'show');
set(legend1,'Location','southeast','AutoUpdate','off');