import numpy as np
from matplotlib import pyplot as plt
import seaborn
import os
import logging

global logger
# setting up log
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('statics_log.log')
logger.addHandler(handler)

'''
This project  is to generate, save, load, manipulate, display a random middle school students' weight and height data. 
Default is a middle school with 100 students. 
The saving file is created under the same directory as this program file, 
and 'named middle_school_student_weight_height.npz'".
The logging file is created under the same directory as this program file, 
and named 'statics_log.log. 
The logging level is defaulted as debug level. 
The standard difference, mean, median, min, max, peak to peak of the weight and height data are calculated 
and logged into the logging file. 
'''


def generate_initial_data(number_of_student=100):

    # generate data
    middle_school_student_weight = np.random.randint(40, 100, number_of_student)
    middle_school_student_weight_array = np.array(middle_school_student_weight)
    middle_school_student_height = np.random.randint(130, 185, number_of_student)
    middle_school_student_height_array = np.array(middle_school_student_height)

    # save data
    file = os.getcwd()+'/middle_school_student_weight_height.npz'
    if os.path.exists(file):
        os.remove(file)
    np.savez("middle_school_student_weight_height.npz",
             weight=middle_school_student_weight_array,
             height=middle_school_student_height_array)

    # load data
    data = np.load("middle_school_student_weight_height.npz")
    weight = data["weight"]
    height = data["height"]
    logger.info("first ten weight data: %s", weight[:10:])
    logger.info("first ten height data: %s", height[:10:])

    # manipulate data
    # standard
    weight_standard = np.std(weight)
    logger.info('weight standard: %s', weight_standard)
    height_standard = np.std(height)
    logger.info('height standard: %s', height_standard)
    # mean
    weight_mean = np.mean(weight)
    logger.info('weight mean: %s', weight_mean)
    height_mean = np.mean(height)
    logger.info('height mean: %s', height_mean)
    # median
    weight_median = np.median(weight)
    logger.info('weight median: %s', weight_median)
    height_median = np.median(height)
    logger.info('height median: %s', height_median)
    # min
    weight_min = np.min(weight)
    logger.info('weight min: %s', weight_min)
    height_min = np.min(height)
    logger.info('height min: %s', height_min)
    # max
    weight_max = np.max(weight)
    logger.info('weight max: %s', weight_max)
    height_max = np.max(height)
    logger.info('height max: %s', height_max)
    # peak to peak
    weight_ptp = np.ptp(weight)
    logger.info('weight ptp: %s', weight_ptp)
    height_ptp = np.ptp(height)
    logger.info('height ptp: %s', height_ptp)
    # number of sample
    logger.info('number of height data of students: %s', np.size(middle_school_student_height))
    logger.info('number of weight data of students: %s', np.size(middle_school_student_weight))

    # display data
    seaborn.set()
    plt.title("Middle Schoolers Weight and Height")
    plt.xlabel("height(cm)/weight(kg)")
    plt.ylabel("number of middle schoolers")
    plt.hist(weight)
    plt.hist(height)
    plt.show()

    logger.debug("entire weight data: %s", weight)
    logger.debug("entire height data: %s", height)
    logger.debug(' ')
    logger.debug(' ')

    return middle_school_student_height_array, middle_school_student_weight_array


def generate_more_data(middle_school_student_height, middle_school_student_weight, number_of_student=10):

    # generate data
    additional_weight_data = np.random.randint(40, 100, number_of_student)
    additional_weight_data_array = np.array(additional_weight_data)
    additional_height_data = np.random.randint(130, 185, number_of_student)
    additional_height_data_array = np.array(additional_height_data)
    middle_school_student_weight_array = np.concatenate((middle_school_student_weight, additional_weight_data_array))
    middle_school_student_height_array = np.concatenate((middle_school_student_height, additional_height_data_array))


    # save data
    log_file_name = 'middle_school_student_weight_height.npz'
    file = os.getcwd()+'/'+log_file_name
    if os.path.exists(file):
        os.remove(file)
    np.savez(log_file_name,
             weight=middle_school_student_weight_array,
             height=middle_school_student_height_array)

    # load data
    data = np.load("middle_school_student_weight_height.npz")
    weight = data["weight"]
    height = data["height"]
    logger.info("first ten weight data: %s", weight[:10:])
    logger.info("first ten height data: %s", height[:10:])

    # manipulate data
    # standard
    weight_standard = np.std(weight)
    logger.info('weight standard: %s', weight_standard)
    height_standard = np.std(height)
    logger.info('height standard: %s', height_standard)
    # mean
    weight_mean = np.mean(weight)
    logger.info('weight mean: %s', weight_mean)
    height_mean = np.mean(height)
    logger.info('height mean: %s', height_mean)
    # median
    weight_median = np.median(weight)
    logger.info('weight median: %s', weight_median)
    height_median = np.median(height)
    logger.info('height median: %s', height_median)
    # min
    weight_min = np.min(weight)
    logger.info('weight min: %s', weight_min)
    height_min = np.min(height)
    logger.info('height min: %s', height_min)
    # max
    weight_max = np.max(weight)
    logger.info('weight max: %s', weight_max)
    height_max = np.max(height)
    logger.info('height max: %s', height_max)
    # peak to peak
    weight_ptp = np.ptp(weight)
    logger.info('weight ptp: %s', weight_ptp)
    height_ptp = np.ptp(height)
    logger.info('height ptp: %s', height_ptp)
    # number of sample
    logger.info('number of height data of students: %s', np.size(middle_school_student_height))
    logger.info('number of weight data of students: %s', np.size(middle_school_student_weight))

    # display data
    seaborn.set()
    plt.title("Middle Schoolers Weight and Height")
    plt.xlabel("height(cm)/weight(kg)")
    plt.ylabel("number of middle schoolers")
    plt.hist(weight)
    plt.hist(height)
    plt.show()


    logger.info('number of height data of students: %s', np.size(middle_school_student_height_array))
    logger.info('number of weight data of students: %s', np.size(middle_school_student_weight_array))

    logger.debug("entire weight data: %s", weight)
    logger.debug("entire height data: %s", height)
    logger.debug(' ')
    logger.debug(' ')

if __name__ == '__main__':
    height, weight = generate_initial_data(30)
    for i in range(1, 11):
        generate_more_data(height, weight, 10)
        print(i)