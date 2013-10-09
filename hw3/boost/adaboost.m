% pdf p8
function [ mu sigma p alpha, classes ] = adaboost( data, T )
%upgrade T times
    [M N] = size(data);
    w = ones(M, 1) / M; %initial
    mu = zeros(2, 2, T);
    sigma = zeros(2, 2, T);
    p = zeros(T,2);
    alpha = zeros(T,1);
    classes = [0; 1];
    for t=1:T
%Extend the old bayes function to bayes_weight(data, w) that handles weighted instances.
        [mu(:,:,t) sigma(:,:,t)] = bayes_weight(data, w);
        p(t,:) = prior(data, w);
        g = discriminant(data(:,1:2), mu(:,:,t), sigma(:,:,t), p(t,:));

%Test
        [dummy class] = max(g, [], 2);

% error e, which is computed value of weak hypothesis ht
        delta = ((class - 1) == (data(:,end))); % error_test
        e = 1.0 - sum(delta .* w);

% choose alpha
        alpha(t) = 0.5 * log((1 - e) / e);

% regarding delta = 1 if ht == cm
% regarding delta = 0 if ht ~= cm
        w1 = delta * exp(-alpha(t));
        w2 = (1 - delta) * exp(alpha(t));
        w = w .* (w1 + w2);
        w = w / sum(w);
    end    

end

