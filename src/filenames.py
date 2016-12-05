""" ============= Generates the default filenames ==============="""

import datetime
import os


def fill_tags_and_paths(pars):
    anomalyframework_root=pars.system.anomalyframework_root
    """ Generates all the filenames for running the anomaly framework on a given feature set """
    # name should generally be the feature file (or the videoname if you wish)

    fill_tags(pars.tags, pars.paths.files.infile_features)
    tmp_foldername = '%s/%s_%s_%s/' % (pars.tags.datestring, pars.tags.timestring, pars.tags.name,
                                       pars.tags.processId)
    pars.paths.folders.path_to_tmp = os.path.join(anomalyframework_root, 'data', 'tmp',
                                                tmp_foldername)

    add_per_shuffle_paths(pars.paths, pars.tags.name, pars.paths.folders.path_to_tmp,
                          pars.algorithm.permutations.n_shuffles)

    pars.paths.folders.path_to_results = os.path.join(anomalyframework_root, 'data', 'results',
                                                  pars.tags.datestring, pars.tags.timestring,
                                                  pars.tags.results_name)
    tmp = pars.paths.folders.path_to_results
    cnt = 2
    while os.path.isdir(pars.paths.folders.path_to_tmp):
        pars.paths.folders.pathToTmp = tmp + '_' + str(cnt)
        cnt += 1
    pars.paths.files.an_file = os.path.join(pars.paths.folders.path_to_tmp, 'a_res.mat')


def add_per_shuffle_paths(paths, name, path_to_tmp, n_shuffles):
    file_format_per_shuffle = {}
    folder_format_per_shuffle = {}

    file_format_per_shuffle['shufflenames_libsvm'] = '_'.join([name, '%03d.train'])
    file_format_per_shuffle['shuffle_idxs'] = 'randIdxs_%d.p'
    file_format_per_shuffle['runinfo_fnames'] = '%d.runinfo'
    file_format_per_shuffle['done_files'] = '%d_done'
    file_format_per_shuffle['verbose_fnames'] = '%d_verbose'

    folder_format_per_shuffle['predict_directories'] = '%d_output/'

    for filename_to_generate in file_format_per_shuffle.keys():
        filenames = [os.path.join(path_to_tmp, file_format_per_shuffle[filename_to_generate]) %
                                   s_idx
                     for s_idx in range(n_shuffles)]

        setattr(paths.files, filename_to_generate, filenames)

    for foldername_to_generate in folder_format_per_shuffle.keys():
        foldernames = [os.path.join(path_to_tmp, folder_format_per_shuffle[
            foldername_to_generate]) %
                                   s_idx
                     for s_idx in range(n_shuffles)]

        setattr(paths.folders, foldername_to_generate, foldernames)

    return paths


def fill_tags(tags, infile_features):
    today = datetime.datetime.today()
    tags.name = os.path.splitext(os.path.basename(infile_features))[0]
    tags.datestring = today.strftime('%Y_%m_%d')
    tags.timestring = today.strftime('%H_%M_%S')
    tags.processId = 1
