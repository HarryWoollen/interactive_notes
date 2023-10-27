import numpy as np

seed = 123

def generate_simple_linear_data(seed:int = seed,n:int = 100):
    np.random.seed(seed)
    x = np.linspace(0,10,n)
    # y = b0 + b1x + e
    b_0 = np.random.normal()*10
    b_1 = np.random.normal()*5
    e = np.random.normal(loc = 0, scale = 3, size = n)

    y = b_0 + b_1*x + e

    #Add random variance to the y values.
    return x.flatten(), y.flatten()


def generate_hetroskedastic_data(seed:int = seed,n:int = 100):
    np.random.seed(seed)
    x = np.linspace(0,10,n)
    # y = b0 + b1x + e
    b_0 = np.random.normal()*10
    b_1 = np.random.normal()*5
    e = np.random.normal(loc = 0, scale = 3 + (x**2)/2, size = n)

    y = b_0 + b_1*x + e

    return x.reshape(100,), y.reshape(100,)

def fit_simple_linear_model(X:np.array,Y:np.array) -> np.array:
    """_summary_

    Args:
        X (np.array): _description_
        Y (np.array): _description_

    Returns:
        (np.array)
    """
    #Get means
    x_bar, y_bar = np.mean(X), np.mean(Y)

    SS_xy = np.sum((X - x_bar) * (Y - y_bar))
    SS_xx = np.sum((X - x_bar)**2)

    b_1 = SS_xy / SS_xx 
    b_0 = y_bar - b_1*x_bar

    y_hat = b_0 + b_1*X

    return y_hat

def plot_line_of_best_fit(X:np.array,Y:np.array,y_hat:np.array) -> None:
    """_summary_

    Args:
        X (np.array): _description_
        Y (np.array): _description_
        y_hat (np.array): _description_
    """
    #Plot Data
    plt.scatter(X,Y)
    #Add line
    plt.plot(X,y_hat,color='r')
    plt.show()


def plot_residuals(Y:np.array,y_hat:np.array) -> None:
    """_summary_

    Args:
        Y (np.array): _description_
        y_hat (np.array): _description_
    """
    #Calculate Residuals
    resid = Y - y_hat

    #Plot Residuals
    plt.scatter(X,resid)
    plt.axhline(y=0,color = 'r', linestyle = '-')
    plt.ylabel('Residuals')
    plt.xlabel('X')
    plt.title('Residuals Scatter')
    plt.show()

    #Plot Standardised Residuals
    #Standardise residuals
    std_resid = resid / np.std(resid)
    plt.scatter(X,std_resid)
    plt.axhline(y=0,color = 'r', linestyle = '-')
    plt.ylim(-3.5,3.5)
    plt.ylabel('Standardised Residuals')
    plt.xlabel('X')
    plt.title('Standardised Residual Scatter')
    plt.show()

    #Histogram
    plt.hist(std_resid)
    plt.title('Histogram of Residuals')
    plt.show()

    #Q-Q Plot
    #Generate qq-plot
    # Calculate the quantiles
    quantiles = np.linspace(0.01, 0.99, 100)  # You can adjust the number of points here
    q_norm = np.quantile(np.random.normal(0, 1, 10000), quantiles)  # Quantiles from the standard normal distribution
    q_residuals = np.quantile(std_resid, quantiles)  # Quantiles of the residuals

    # Generate Q-Q plot
    plt.scatter(q_norm, q_residuals)
    plt.plot([-3, 3], [-3, 3], color='r')  # This is the line y = x
    plt.title('Q-Q Plot of Standardized Residuals')
    plt.xlabel('Theoretical Quantiles')
    plt.ylabel('Sample Quantiles')
    plt.show()