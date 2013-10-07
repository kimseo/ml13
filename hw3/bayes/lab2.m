% The best object recognition performance is achieved when the training image shows the book alone. We would like to remove the hand holding the book from the image.

% data import
hand = imread('hand.ppm', 'ppm');
book = imread('book.ppm', 'ppm');
imagesc(hand);
figure;
imagesc(book);

% The function normalize and label computes the normalized red and green intensities.
data1 = normalize_and_label(hand,0);
data2 = normalize_and_label(book,1);
test_data = [data1; data2];
figure;
hold on;

% show plot
plot(data2(:,1), data2(:,2), '.');
plot(data1(:,1), data1(:,2), '.r');
legend('Hand holding book', 'Hand');
xlabel('green');
ylabel('red');

% With P(h) (later in the text p(ci)) we denote the prior probability of a hypothesis/class, before we observe any data.
[mu sigma] = bayes(test_data);

theta = [0:0.01:2*pi];
x1 = 2*sigma(1,1) * cos(theta) + mu(1,1);
y1 = 2*sigma(1,2) * cos(theta) + mu(1,2);
y2 = 2*sigma(2,2) * cos(theta) + mu(2,2);
x2 = 2*sigma(2,1) * cos(theta) + mu(2,1);
plot(x1,y1,'r');
plot(x2,y2);

% Lab assignment 1
% percentage of given class in dataset

% with P (D) (later p(⃗x)) we denote the prior probabilty that training data D will be observed.
p = prior(test_data);

% The likelihood density funtions for a model (hypothesis)
g = discriminant(test_data(:,1:2),mu, sigma, p);


% Lab assignment 2
% Train the Bayes classifier with the dataset test_data, and compute the classification error.
% We use the Matlab function max to compute the maximum discriminant value and the index class of the optimal class, which we compare with the known classification test_data(:,3).
[M N] = size(test_data);
[dummy class] = max(g, [], 2);
class = class - 1;
error_test = 1.0 -sum(class == test_data(:,end))/M;

% print
error_test

% copy codes from pdf (p7)
ax = [0.2 0.5 0.2 0.45];
axis(ax);
x = ax(1):0.01:ax(2);
y = ax(3):0.01:ax(4);
[z1 z2] = meshgrid(x,y);
z1 = reshape(z1, size(z1,1)*size(z1,2), 1);
z2 = reshape(z2, size(z2,1)*size(z2,2), 1);
g = discriminant([z1 z2], mu, sigma, p);
gg = g(:,1) - g(:,2);
gg = reshape(gg, length(y), length(x));
[c,h] = contour(x,y,gg, [0.0 0.0]);
set(h, 'LineWidth', 3);

book_rg = zeros(size(book,1), size(book,2), 2);
for y = 1:size(book,1)
    for x = 1:size(book,2)
        s = sum(book(y,x,:));
        if (s>0)
            book_rg(y,x,:) = [double(book(y,x,1))/s double(book(y,x,2))/s];
        end
    end
end

tmp = reshape(book_rg, size(book_rg,1)*size(book_rg,2),2);
g = discriminant(tmp, mu, sigma, p);
gg = g(:,1) - g(:,2);
gg = reshape(gg, size(book_rg,1), size(book_rg,2));
mask = gg < 0;
mask3D(:,:,1) = mask;
mask3D(:,:,2) = mask;
mask3D(:,:,3) = mask;
result_im = uint8(double(book) .* mask3D);
figure;
imagesc(result_im);
% end of lab assignment 2

