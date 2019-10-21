%% Question 1, part 2 
Q = [ 1 2 0; 2 5 0; 0 0 0];
cvx_begin
    variable x(3)
    maximize -inv_pos(2*x(1)+4*x(3)) - 5*square(x(1)) - 40*square(x(2)) - (43/5)*square(x(3)) - quad_over_lin((x(1)-0.5), x(2)+x(3)) - 0.75*inv_pos(x(2)+x(3))
    subject to
            square_pos(quad_form(x,Q)) - min(x(1)+x(2),sqrt(x(1))) <= 10;
            x >= 1/1000;
cvx_end
x
