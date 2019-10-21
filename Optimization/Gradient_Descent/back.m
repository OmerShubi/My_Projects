function lsearch = back(alpha, beta, s)

    % Input checks
    if alpha<=0 || ~isreal(alpha) || ~isscalar(alpha)
            error("alpha must be a real positive scalar")
    end
    if beta<=0 || ~isreal(beta) || ~isscalar(beta)
            error("beta must be a real positive scalar")
    end
    if s<=0 || ~isreal(s) || ~isscalar(s)
            error("s must be a real positive scalar")
    end

    % Create and then return inner function
    function t_k = Armijio(f,x_k,g_k)
        t_k = s;
        while( f(x_k - t_k*g_k) >= (f(x_k) - alpha*t_k*(norm(g_k)^2)))
            t_k = beta*t_k;
        end
    end

    lsearch=@Armijio;
end
