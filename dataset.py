from icldata import ICLabelDataset

icl = ICLabelDataset(combine_output=True)

icldata = icl.load_semi_supervised()

# import pickle as pkl
# import constant
# from os.path import join

# with open(join('labels', constant.ICLABELS_TEST), 'rb') as f:
#     labels = pkl.load(f,encoding='latin1')
#     print(labels.keys())