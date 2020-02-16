# Train and validaton errors initialized as empty list
train_errs = list()
valid_errs = list()

# Loop over values of C_value
for C_value in [0.001, 0.01, 0.1, 1, 10, 100, 1000]:
    # Create LogisticRegression object and fit
    lr = ____
    lr.fit(____)
    
    # Evaluate error rates and append to lists
    train_errs.append( 1.0 - lr.score(____) )
    valid_errs.append( 1.0 - lr.score(____) )
    
# Plot results
plt.semilogx(C_values, train_errs, C_values, valid_errs)
plt.legend(("train", "validation"))
plt.show()
