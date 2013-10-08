function [mu, sigma] = bayes_weight(data, w)
	mu = zeros(2, 2);
	sigma = zeros(2, 2);
	W1 = 0;
	W2 = 0;
	
	for n = 1:2
		for i = 1:size(data, 1)
			if data(i, 3) == 0.0
				mu(1, n) = mu(1, n) + (w(i) * data(i, n));
				W1 = W1 + w(i);
			elseif data(i, 3) == 1.0
				mu(2, n) = mu(2, n) + (w(i) * data(i, n));
				W2 = W2 + w(i);
			end
		end
		mu(1, n) = mu(1, n) ./ W1;
		mu(2, n) = mu(2, n) ./ W2;
		for i = 1:size(data, 1)
			if data(i, 3) == 0.0
				sigma(1, n) = sigma(1, n) + (w(i) * (data(i, n) - mu(1, n)).^2);
				W1 = W1 + w(i);
			elseif data(i, 3) == 1.0
				sigma(2, n) = sigma(2, n) + (w(i) * (data(i, n) - mu(2, n)).^2);
				W2 = W2 + w(i);
			end
		end
		sigma(1, n) = sqrtm(sigma(1, n) ./ W1);
		sigma(2, n) = sqrtm(sigma(2, n) ./ W2);
	end
end
