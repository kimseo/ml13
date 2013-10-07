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