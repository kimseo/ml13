function [mu, sigma] = bayes(data)
	mu = zeros(2, 2);
	sigma = zeros(2, 2);
	M1 = 0;
	M2 = 0;

	for i = 1:size(data, 1)
		if data(i, 3) == 0.0
			M1 = M1 + 1;
		elseif data(i, 3) == 1.0
			M2 = M2 + 1;
		end
	end
	
	for n = 1:2
		for i = 1:size(data, 1)
			if data(i, 3) == 0.0
				mu(1, n) = mu(1, n) + data(i, n);
			elseif data(i, 3) == 1.0
				mu(2, n) = mu(2, n) + data(i, n);
			end
		end
		mu(1, n) = mu(1, n) ./ M1;
		mu(2, n) = mu(2, n) ./ M2;
		for i = 1:size(data, 1)
			if data(i, 3) == 0.0
				sigma(1, n) = sigma(1, n) + (data(i, n) - mu(1, n)).^2;
			elseif data(i, 3) == 1.0
				sigma(2, n) = sigma(2, n) + (data(i, n) - mu(2, n)).^2;
			end
		end
		sigma(1, n) = sqrtm(sigma(1, n) ./ M1);
		sigma(2, n) = sqrtm(sigma(2, n) ./ M2);
	end
end