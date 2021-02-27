import numpy as np

if __name__ == "__main__":
    x1 = np.array([19,39,30,30,15,15,15,30])
    x2 = np.array([63,74,87,23,35,43,32,73])
    m1 = np.round(np.mean(x1),1)
    m2 = np.round(np.mean(x2),1)
    print("Mean of X1: ", m1)
    print("Mean of X2: ", m2)
    Xm1 = x1 - m1
    Xm2 = x2 - m2
    print("X1': ", Xm1)
    print("X2': ", Xm2)

    cov1 = np.round(np.cov(Xm1,np.transpose(Xm2)),2)
    print("Covariance: \n",cov1)

    eigval, eigvec = np.linalg.eig(cov1)
    print("Eigenvalues: \n", np.round(eigval,2))
    print("Eigenvector: \n", np.round(eigvec,2))

    pca = np.array([])
    # for i in range(0,np.size(x1)):
    y1 = (0.89 * 7)
    y2 = (0.45 * 2)
    y = y1 + y2
    pca = np.append(pca,y)

    print("PCA: \n", pca)