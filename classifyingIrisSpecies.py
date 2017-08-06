from sklearn.datasets import load_iris
iris_dataset = load_iris()

print "Keys of iris_dataset: \n{}".format(iris_dataset.keys())


print iris_dataset['DESCR'][:193] + "\n..."


print "Target names: {}".format(iris_dataset['target_names'])

print "Feature names: \n{}".format(iris_dataset['feature_names'])

print "Type of data: {}".format(type(iris_dataset))

