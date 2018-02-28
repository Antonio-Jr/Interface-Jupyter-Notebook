import ast, json
import logging
import sys

import itertools

from collections import defaultdict

arquivo = {'wnn-harem_second-epochs_100-batch_size_8-hidden_size_100.log': {u'timestamp': set([u'2017/07/24 16:31:29', u'2017/07/24 16:29:59', u'2017/07/24 16:22:16', u'2017/07/24 16:28:00', u'2017/07/24 16:31:22',
                           u'2017/07/24 16:28:07', u'2017/07/24 16:30:12', u'2017/07/24 16:25:48', u'2017/07/24 16:27:32', u'2017/07/24 16:34:22',
                           u'2017/07/24 16:27:39', u'2017/07/24 16:30:19', u'2017/07/24 16:30:54', u'2017/07/24 16:30:26', u'2017/07/24 16:34:29',
                           u'2017/07/24 16:25:13', u'2017/07/24 16:30:47', u'2017/07/24 16:33:40', u'2017/07/24 16:21:02', u'2017/07/24 16:23:53',
                           u'2017/07/24 16:24:21', u'2017/07/24 16:32:38', u'2017/07/24 16:22:58', u'2017/07/24 16:29:38', u'2017/07/24 16:28:49',
                           u'2017/07/24 16:33:06', u'2017/07/24 16:26:30', u'2017/07/24 16:26:37', u'2017/07/24 16:28:42', u'2017/07/24 16:34:50',
                           u'2017/07/24 16:28:56', u'2017/07/24 16:31:57', u'2017/07/24 16:31:36', u'2017/07/24 16:34:15', u'2017/07/24 16:31:01',
                           u'2017/07/24 16:31:43', u'2017/07/24 16:23:11', u'2017/07/24 16:27:25', u'2017/07/24 16:30:05', u'2017/07/24 16:25:34',
                           u'2017/07/24 16:30:40', u'2017/07/24 16:29:31', u'2017/07/24 16:25:06', u'2017/07/24 16:21:32', u'2017/07/24 16:32:24',
                           u'2017/07/24 16:25:00', u'2017/07/24 16:21:39', u'2017/07/24 16:24:34', u'2017/07/24 16:33:54', u'2017/07/24 16:29:10',
                           u'2017/07/24 16:26:02', u'2017/07/24 16:33:13', u'2017/07/24 16:27:11', u'2017/07/24 16:26:09', u'2017/07/24 16:26:44',
                           u'2017/07/24 16:29:24', u'2017/07/24 16:27:53', u'2017/07/24 16:29:03', u'2017/07/24 16:34:43', u'2017/07/24 16:34:08',
                           u'2017/07/24 16:28:21', u'2017/07/24 16:31:15', u'2017/07/24 16:29:52', u'2017/07/24 16:34:01', u'2017/07/24 16:22:30',
                           u'2017/07/24 16:31:08', u'2017/07/24 16:30:33', u'2017/07/24 16:34:57', u'2017/07/24 16:25:27', u'2017/07/24 16:25:20',
                           u'2017/07/24 16:32:17', u'2017/07/24 16:25:41', u'2017/07/24 16:27:18', u'2017/07/24 16:32:10', u'2017/07/24 16:33:26',
                           u'2017/07/24 16:24:07', u'2017/07/24 16:33:20', u'2017/07/24 16:32:52', u'2017/07/24 16:26:58', u'2017/07/24 16:26:16',
                           u'2017/07/24 16:32:59', u'2017/07/24 16:29:17', u'2017/07/24 16:23:25', u'2017/07/24 16:26:51', u'2017/07/24 16:24:46',
                           u'2017/07/24 16:28:35', u'2017/07/24 16:22:02', u'2017/07/24 16:27:46', u'2017/07/24 16:27:05', u'2017/07/24 16:29:45',
                           u'2017/07/24 16:28:28', u'2017/07/24 16:33:47', u'2017/07/24 16:25:55', u'2017/07/24 16:34:36', u'2017/07/24 16:23:39',
                           u'2017/07/24 16:28:14', u'2017/07/24 16:32:04', u'2017/07/24 16:33:33', u'2017/07/24 16:32:45', u'2017/07/24 16:26:23',
                           u'2017/07/24 16:31:50', u'2017/07/24 16:32:31', u'2017/07/24 16:24:53', u'2017/07/24 16:22:44']), u'message': {
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 94, u'type': u'duration', u'iteration': 894615}",
            "{u'name': u'CustomMetricDev', u'iteration': 329595, u'subtype': u'evaluation', u'epoch': 34, u'values': {u'truePositives': 76, "
            "u'numExamples': ""455, u'micro': {u'recall': 0.4175824175824176, u'precision': 0.2177650429799427, u'f': 0.2862523540489642}, "
            "u'macro': {u'recall': "
            "0.20686026936026936, u'precision': 0.11738162212845757, u'f': 0.14977456404507988}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 55, u'2': 0, "
            "u'4': 21}, u'f': {u'1': 0, u'3': 0.291005291005291, u'2': 0, u'4': 0.28965517241379307}, u'recall': {u'1': 0.0, "
            "u'3': 0.5092592592592593, "
            "u'2': 0.0, u'4': 0.3181818181818182}, u'precision': {u'1': 0, u'3': 0.2037037037037037, u'2': 0, u'4': 0.26582278481012656}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 53, u'2': 4, u'4': 45}, u'falsePositives': {u'3': 215, u'4': 58}}, u'falseNegatives': 106, u'beta': 1.0, u'numLabels': "
            "4, "
            "u'falsePositives': 76}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 55, u'type': u'duration', u'iteration': 527352}",
            "{u'name': u'AccDev', u'iteration': 75336, u'subtype': u'evaluation', u'epoch': 7, u'values': {u'accumAccuracy': 4158.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8720637583892618}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 244842, u'subtype': u'train', u'epoch': 25, u'values': {u'accumAccuracy': 68070.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9035640804406982}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 941700, u'subtype': u'evaluation', u'epoch': 99, u'values': {u'loss': 0.1890828013420105, "
            "u'accumLoss': "
            "901.546796798706, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 28251, u'subtype': u'train', u'epoch': 2, u'values': {u'loss': 0.5020740655530794, u'accumLoss': "
            "37823.74972844124, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 141255, u'subtype': u'evaluation', u'epoch': 14, u'values': {u'accumAccuracy': 4205.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8819211409395973}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 48, u'type': u'duration', u'iteration': 461433}",
            "{u'name': u'FMetricDev', u'iteration': 160089, u'subtype': u'evaluation', u'epoch': 16, u'values': {u'truePositives': 4204, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8817114093959731, u'precision': 0.8817114093959731, u'f': 0.8817114093959733}, u'macro': {u'recall': "
            "0.30050687639830265, "
            "u'precision': 0.44493498070804527, u'f': 0.35872957757411966}, u'perLabel': {u'truePositives': {u'0': 4088, u'3': 113, u'4': 3}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9608649665060524, u'3': 0.3668831168831168, u'2': 0, u'4': 0.03076923076923077}, u'recall': {u'1': 0.0, "
            "u'0': 0.9891120251633196, "
            "u'3': 0.4977973568281938, u'2': 0.0, u'4': 0.015625}, u'precision': {u'1': 0, u'0': 0.9341864716636198, u'3': 0.29048843187660667, "
            "u'2': 0, "
            "u'4': 1.0}, u'falseNegatives': {u'1': 119, u'0': 45, u'3': 114, u'2': 97, u'4': 189}, u'falsePositives': {u'0': 288, u'3': 276}}, "
            "u'falseNegatives': 564, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4204}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 9417, u'subtype': u'train', u'epoch': 0, u'values': {u'accumAccuracy': 65313.0, u'numExamples': "
            "75335, "
            "u'accuracy': 0.8669675449658193}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 800445, u'subtype': u'evaluation', u'epoch': 84, u'values': {u'truePositives': 4434, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9299496644295302, u'precision': 0.9299496644295302, u'f': 0.9299496644295302}, u'macro': {u'recall': "
            "0.5541894095208472, "
            "u'precision': 0.6024657176058021, u'f': 0.5773200887042872}, u'perLabel': {u'truePositives': {u'1': 20, u'0': 4076, u'3': 179, "
            "u'4': 159}, "
            "u'f': {u'1': 0.26845637583892623, u'0': 0.9774580335731415, u'3': 0.62478184991274, u'2': 0, u'4': 0.8435013262599469}, "
            "u'recall': {u'1': "
            "0.16806722689075632, u'0': 0.9862085652068715, u'3': 0.788546255506608, u'2': 0.0, u'4': 0.828125}, u'precision': {u'1': "
            "0.6666666666666666, "
            "u'0': 0.9688614214404564, u'3': 0.5173410404624278, u'2': 0, u'4': 0.8594594594594595}, u'falseNegatives': {u'1': 99, u'0': 57, "
            "u'3': 48, "
            "u'2': 97, u'4': 33}, u'falsePositives': {u'1': 10, u'0': 131, u'3': 167, u'4': 26}}, u'falseNegatives': 334, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4434}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 339012, u'subtype': u'evaluation', u'epoch': 35, u'values': {u'truePositives': 4347, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9117030201342282, u'precision': 0.9117030201342282, u'f': 0.9117030201342282}, u'macro': {u'recall': "
            "0.4495119352917832, "
            "u'precision': 0.43759536526064247, u'f': 0.44347361224630444}, u'perLabel': {u'truePositives': {u'0': 4081, u'3': 156, u'4': 110}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9722453841572364, u'3': 0.5226130653266331, u'2': 0, u'4': 0.6707317073170731}, u'recall': {u'1': 0.0, "
            "u'0': 0.9874183401887249, "
            "u'3': 0.6872246696035242, u'2': 0.0, u'4': 0.5729166666666666}, u'precision': {u'1': 0, u'0': 0.9575316752698264, "
            "u'3': 0.42162162162162165, "
            "u'2': 0, u'4': 0.8088235294117647}, u'falseNegatives': {u'1': 119, u'0': 52, u'3': 71, u'2': 97, u'4': 82}, u'falsePositives': {u'0': "
            "181, "
            "u'3': 214, u'4': 26}}, u'falseNegatives': 421, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4347}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 216591, u'subtype': u'evaluation', u'epoch': 22, u'values': {u'accumAccuracy': 4248.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8909395973154363}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 781611, u'subtype': u'evaluation', u'epoch': 82, u'values': {u'truePositives': 4428, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9286912751677853, u'precision': 0.9286912751677853, u'f': 0.9286912751677853}, u'macro': {u'recall': "
            "0.5537134817959027, "
            "u'precision': 0.5888163811868138, u'f': 0.5707256836407893}, u'perLabel': {u'truePositives': {u'1': 15, u'0': 4066, u'3': 185, "
            "u'4': 162}, "
            "u'f': {u'1': 0.2097902097902098, u'0': 0.9779915814792544, u'3': 0.6187290969899665, u'2': 0, u'4': 0.8459530026109662}, "
            "u'recall': {u'1': "
            "0.12605042016806722, u'0': 0.9837890152431648, u'3': 0.8149779735682819, u'2': 0.0, u'4': 0.84375}, u'precision': {u'1': 0.625, "
            "u'0': 0.9722620755619321, u'3': 0.49865229110512127, u'2': 0, u'4': 0.8481675392670157}, u'falseNegatives': {u'1': 104, u'0': 67, "
            "u'3': 42, "
            "u'2': 97, u'4': 30}, u'falsePositives': {u'1': 9, u'0': 116, u'3': 186, u'4': 29}}, u'falseNegatives': 340, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4428}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 95, u'type': u'duration', u'iteration': 904032}",
            "{u'name': u'LossDev', u'iteration': 885198, u'subtype': u'evaluation', u'epoch': 93, u'values': {u'loss': 0.19227167963981628, "
            "u'accumLoss': "
            "916.751368522644, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 188340, u'subtype': u'train', u'epoch': 19, u'values': {u'loss': 0.2897318448079438, "
            "u'accumLoss': "
            "21826.948528606445, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 21, u'type': u'duration', u'iteration': 207174}",
            "{u'name': u'AccDev', u'iteration': 244842, u'subtype': u'evaluation', u'epoch': 25, u'values': {u'accumAccuracy': 4282.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8980704697986577}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 62, u'type': u'duration', u'iteration': 593271}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 33, u'type': u'duration', u'iteration': 320178}",
            "{u'name': u'FMetricDev', u'iteration': 480267, u'subtype': u'evaluation', u'epoch': 50, u'values': {u'truePositives': 4381, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9188338926174496, u'precision': 0.9188338926174496, u'f': 0.9188338926174496}, u'macro': {u'recall': "
            "0.49197038946937954, "
            "u'precision': 0.45189695232931887, u'f': 0.4710829791267331}, u'perLabel': {u'truePositives': {u'0': 4071, u'3': 174, u'4': 136}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9752066115702479, u'3': 0.5621970920840064, u'2': 0, u'4': 0.7727272727272727}, u'recall': {u'1': 0.0, "
            "u'0': 0.9849987902250181, "
            "u'3': 0.7665198237885462, u'2': 0.0, u'4': 0.7083333333333334}, u'precision': {u'1': 0, u'0': 0.9656072106261859, "
            "u'3': 0.44387755102040816, "
            "u'2': 0, u'4': 0.85}, u'falseNegatives': {u'1': 119, u'0': 62, u'3': 53, u'2': 97, u'4': 56}, u'falsePositives': {u'0': 145, u'3': 218, "
            "u'4': 24}}, u'falseNegatives': 387, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4381}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 574437, u'subtype': u'train', u'epoch': 60, u'values': {u'accumAccuracy': 70275.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9328333443950355}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 103587, u'subtype': u'evaluation', u'epoch': 10, u'values': {u'truePositives': 4190, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8787751677852349, u'precision': 0.8787751677852349, u'f': 0.8787751677852349}, u'macro': {u'recall': "
            "0.2776025293907218, "
            "u'precision': 0.4579301324071071, u'f': 0.345661232037531}, u'perLabel': {u'truePositives': {u'1': 2, u'0': 4103, u'3': 80, u'4': 5}, "
            "u'f': {u'1': 0.02564102564102564, u'0': 0.9532992565055762, u'3': 0.33472803347280333, u'2': 0, u'4': 0.050761421319796954}, "
            "u'recall': {u'1': "
            "0.01680672268907563, u'0': 0.9927413501088798, u'3': 0.3524229074889868, u'2': 0.0, u'4': 0.026041666666666668}, u'precision': {u'1': "
            "0.05405405405405406, u'0': 0.9168715083798883, u'3': 0.3187250996015936, u'2': 0, u'4': 1.0}, u'falseNegatives': {u'1': 117, u'0': 30, "
            "u'3': 147, "
            "u'2': 97, u'4': 187}, u'falsePositives': {u'1': 35, u'0': 372, u'3': 171}}, u'falseNegatives': 578, u'beta': 1.0, u'numLabels': 5, "
            "u'falsePositives': 4190}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 28251, u'subtype': u'evaluation', u'epoch': 2, u'values': {u'loss': 0.48963451385498047, "
            "u'accumLoss': "
            "2334.577362060547, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 753360, u'subtype': u'train', u'epoch': 79, u'values': {u'accumAccuracy': 70797.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9397623946372868}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 442599, u'subtype': u'train', u'epoch': 46, u'values': {u'loss': 0.21211513633534093, "
            "u'accumLoss': "
            "15979.69379582291, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 706275, u'subtype': u'evaluation', u'epoch': 74, u'values': {u'truePositives': 4418, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9265939597315436, u'precision': 0.9265939597315436, u'f': 0.9265939597315436}, u'macro': {u'recall': "
            "0.5374431789117425, "
            "u'precision': 0.6062616774061833, u'f': 0.5697819701606133}, u'perLabel': {u'truePositives': {u'1': 10, u'0': 4069, u'3': 183, "
            "u'4': 156}, "
            "u'f': {u'1': 0.15037593984962405, u'0': 0.9770680753992076, u'3': 0.6059602649006622, u'2': 0, u'4': 0.8364611260053619}, "
            "u'recall': {u'1': "
            "0.08403361344537816, u'0': 0.9845148802322768, u'3': 0.8061674008810573, u'2': 0.0, u'4': 0.8125}, u'precision': {u'1': "
            "0.7142857142857143, "
            "u'0': 0.9697330791229742, u'3': 0.4854111405835544, u'2': 0, u'4': 0.861878453038674}, u'falseNegatives': {u'1': 109, u'0': 64, "
            "u'3': 44, "
            "u'2': 97, u'4': 36}, u'falsePositives': {u'1': 4, u'0': 127, u'3': 194, u'4': 25}}, u'falseNegatives': 350, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4418}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 696858, u'subtype': u'evaluation', u'epoch': 73, u'values': {u'truePositives': 112, "
            "u'numExamples': "
            "450, u'micro': {u'recall': 0.4444444444444444, u'precision': 0.36129032258064514, u'f': 0.39857651245551595}, u'macro': {u'recall': "
            "0.3186709436709437, u'precision': 0.41504329004329005, u'f': 0.3605279298804002}, u'perLabel': {u'truePositives': {u'1': 6, u'3': 70, "
            "u'2': 0, "
            "u'4': 36}, u'f': {u'1': 0.14814814814814817, u'3': 0.41297935103244837, u'2': 0, u'4': 0.5217391304347826}, u'recall': {u'1': "
            "0.08108108108108109, "
            "u'3': 0.6481481481481481, u'2': 0.0, u'4': 0.5454545454545454}, u'precision': {u'1': 0.8571428571428571, u'3': 0.30303030303030304, "
            "u'2': 0, "
            "u'4': 0.5}, u'falseNegatives': {u'1': 68, u'3': 38, u'2': 4, u'4': 30}, u'falsePositives': {u'1': 1, u'3': 161, u'4': 36}}, "
            "u'falseNegatives': "
            "140, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 112}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 28, u'type': u'duration', u'iteration': 273093}",
            "{u'name': u'LossDev', u'iteration': 423765, u'subtype': u'evaluation', u'epoch': 44, u'values': {u'loss': 0.24720600247383118, "
            "u'accumLoss': "
            "1178.678219795227, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 263676, u'subtype': u'evaluation', u'epoch': 27, u'values': {u'loss': 0.28905466198921204, "
            "u'accumLoss': "
            "1378.212628364563, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 15, u'type': u'duration', u'iteration': 150672}",
            "{u'learn_rate': [0.001], u'epoch': 6, u'iteration': 56502}", u'Size of word lexicon is 453991 and word embedding size is 100',
            "{u'name': u'AccDev', u'iteration': 932283, u'subtype': u'evaluation', u'epoch': 98, u'values': {u'accumAccuracy': 4453.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9339345637583892}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 932283, u'subtype': u'train', u'epoch': 98, u'values': {u'accumAccuracy': 71344.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.94702329594478}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 103587, u'subtype': u'evaluation', u'epoch': 10, u'values': {u'accumAccuracy': 4190.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8787751677852349}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 452016, u'subtype': u'train', u'epoch': 47, u'values': {u'accumAccuracy': 69771.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9261432269197584}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 5, u'iteration': 47085}",
            "{u'name': u'AccDev', u'iteration': 329595, u'subtype': u'evaluation', u'epoch': 34, u'values': {u'accumAccuracy': 4343.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9108640939597316}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 621522, u'subtype': u'train', u'epoch': 65, u'values': {u'accumAccuracy': 70420.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9347580805734387}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 536769, u'subtype': u'train', u'epoch': 56, u'values': {u'loss': 0.19174141974579564, "
            "u'accumLoss': "
            "14444.839856549515, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 75336, u'subtype': u'evaluation', u'epoch': 7, u'values': {u'truePositives': 6, "
            "u'numExamples': 393, "
            "u'micro': {u'recall': 0.023809523809523808, u'precision': 0.04081632653061224, u'f': 0.030075187969924814}, u'macro': {u'recall': "
            "0.016016016016016016, u'precision': 0.022233201581027668, u'f': 0.018619325308059327}, u'perLabel': {u'truePositives': {u'1': 2, "
            "u'3': 4, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0.03333333333333333, u'3': 0.04081632653061224, u'2': 0, u'4': 0}, u'recall': {u'1': 0.02702702702702703, "
            "u'3': 0.037037037037037035, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0.043478260869565216, u'3': 0.045454545454545456, u'2': 0, "
            "u'4': 0.0}, "
            "u'falseNegatives': {u'1': 72, u'3': 104, u'2': 4, u'4': 66}, u'falsePositives': {u'1': 44, u'3': 84, u'4': 13}}, u'falseNegatives': "
            "246, "
            "u'beta': 1.0, u'numLabels': 4, u'falsePositives': 6}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 404931, u'subtype': u'evaluation', u'epoch': 42, u'values': {u'truePositives': 4357, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9138003355704698, u'precision': 0.9138003355704698, u'f': 0.9138003355704698}, u'macro': {u'recall': "
            "0.4664293227160923, "
            "u'precision': 0.4371780152753331, u'f': 0.4513302116924023}, u'perLabel': {u'truePositives': {u'0': 4073, u'3': 165, u'4': 119}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9734703632887189, u'3': 0.5409836065573771, u'2': 0, u'4': 0.695906432748538}, u'recall': {u'1': 0.0, u'0': 0.9854827002177595, "
            "u'3': 0.7268722466960352, u'2': 0.0, u'4': 0.6197916666666666}, u'precision': {u'1': 0, u'0': 0.9617473435655254, "
            "u'3': 0.4308093994778068, "
            "u'2': 0, u'4': 0.7933333333333333}, u'falseNegatives': {u'1': 119, u'0': 60, u'3': 62, u'2': 97, u'4': 73}, u'falsePositives': {u'0': "
            "162, "
            "u'3': 218, u'4': 31}}, u'falseNegatives': 411, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4357}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 885198, u'subtype': u'evaluation', u'epoch': 93, u'values': {u'accumAccuracy': 4444.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9320469798657718}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 103587, u'subtype': u'evaluation', u'epoch': 10, u'values': {u'truePositives': 23, "
            "u'numExamples': "
            "460, u'micro': {u'recall': 0.09126984126984126, u'precision': 0.09956709956709957, u'f': 0.09523809523809523}, u'macro': {u'recall': "
            "0.0543043043043043, u'precision': 0.035857285857285856, u'f': 0.04319366948232928}, u'perLabel': {u'truePositives': {u'1': 1, "
            "u'3': 22, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0.01801801801801802, u'3': 0.14814814814814814, u'2': 0, u'4': 0}, u'recall': {u'1': 0.013513513513513514, "
            "u'3': 0.2037037037037037, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0.02702702702702703, u'3': 0.1164021164021164, u'2': 0, "
            "u'4': 0.0}, "
            "u'falseNegatives': {u'1': 73, u'3': 86, u'2': 4, u'4': 66}, u'falsePositives': {u'1': 36, u'3': 167, u'4': 5}}, u'falseNegatives': 229, "
            "u'beta': 1.0, u'numLabels': 4, u'falsePositives': 23}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 291927, u'subtype': u'evaluation', u'epoch': 30, u'values': {u'accumAccuracy': 4322.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9064597315436241}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 894615, u'subtype': u'train', u'epoch': 94, u'values': {u'loss': 0.1493602448959923, "
            "u'accumLoss': "
            "11252.054049239581, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 8, u'type': u'duration', u'iteration': 84753}",
            "{u'name': u'FMetricDev', u'iteration': 461433, u'subtype': u'evaluation', u'epoch': 48, u'values': {u'truePositives': 4377, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.917994966442953, u'precision': 0.917994966442953, u'f': 0.9179949664429529}, u'macro': {u'recall': "
            "0.48431244832697534, "
            "u'precision': 0.4514934418770674, u'f': 0.4673274586706824}, u'perLabel': {u'truePositives': {u'0': 4075, u'3': 171, u'4': 131}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9747637842363354, u'3': 0.5579119086460032, u'2': 0, u'4': 0.7572254335260116}, u'recall': {u'1': 0.0, "
            "u'0': 0.9859666102105008, "
            "u'3': 0.7533039647577092, u'2': 0.0, u'4': 0.6822916666666666}, u'precision': {u'1': 0, u'0': 0.9638126773888364, "
            "u'3': 0.4430051813471503, "
            "u'2': 0, u'4': 0.8506493506493507}, u'falseNegatives': {u'1': 119, u'0': 58, u'3': 56, u'2': 97, u'4': 61}, u'falsePositives': {u'0': "
            "153, "
            "u'3': 215, u'4': 23}}, u'falseNegatives': 391, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4377}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 216591, u'subtype': u'train', u'epoch': 22, u'values': {u'accumAccuracy': 67766.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.8995287714873564}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 40, u'iteration': 376680}",
            "{u'name': u'LossTrain', u'iteration': 433182, u'subtype': u'train', u'epoch': 45, u'values': {u'loss': 0.21448637269972112, "
            "u'accumLoss': "
            "16158.33088733349, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 73, u'type': u'duration', u'iteration': 696858}",
            "{u'name': u'LossDev', u'iteration': 856947, u'subtype': u'evaluation', u'epoch': 90, u'values': {u'loss': 0.19390878081321716, "
            "u'accumLoss': "
            "924.5570669174194, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 90, u'type': u'duration', u'iteration': 856947}",
            "{u'name': u'LossDev', u'iteration': 404931, u'subtype': u'evaluation', u'epoch': 42, u'values': {u'loss': 0.2524596154689789, "
            "u'accumLoss': "
            "1203.7274465560913, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 386097, u'subtype': u'evaluation', u'epoch': 40, u'values': {u'accumAccuracy': 4355.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9133808724832215}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 150672, u'subtype': u'train', u'epoch': 15, u'values': {u'loss': 0.3066038829658267, "
            "u'accumLoss': "
            "23098.003523230553, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 583854, u'subtype': u'train', u'epoch': 61, u'values': {u'loss': 0.1835904280317515, "
            "u'accumLoss': "
            "13830.784895771998, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 44, u'iteration': 414348}",
            "{u'name': u'AccDev', u'iteration': 131838, u'subtype': u'evaluation', u'epoch': 13, u'values': {u'accumAccuracy': 4198.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8804530201342282}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 659190, u'subtype': u'evaluation', u'epoch': 69, u'values': {u'loss': 0.20866639912128448, "
            "u'accumLoss': "
            "994.9213910102844, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 6, u'subtype': u'training', u'epoch': 32, u'type': u'duration', u'iteration': 310761}", u'Number of tokens read: 75335',
            "{u'name': u'AccTrain', u'iteration': 103587, u'subtype': u'train', u'epoch': 10, u'values': {u'accumAccuracy': 66472.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.8823521603504347}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 37668, u'subtype': u'evaluation', u'epoch': 3, u'values': {u'truePositives': 4133, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8668204697986577, u'precision': 0.8668204697986577, u'f': 0.8668204697986577}, u'macro': {u'recall': 0.2, "
            "u'precision': "
            "0.17380151387720774, u'f': 0.1859826752165598}, u'perLabel': {u'truePositives': {u'0': 4133}, u'f': {u'1': 0, u'0': 0.929913376082799, "
            "u'3': 0, "
            "u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'0': 1.0, u'3': 0.0, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0.0, "
            "u'0': 0.8690075693860387, "
            "u'3': 0.0, u'2': 0, u'4': 0}, u'falseNegatives': {u'1': 119, u'3': 227, u'2': 97, u'4': 192}, u'falsePositives': {u'1': 2, u'0': 623, "
            "u'3': 10}}, "
            "u'falseNegatives': 635, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4133}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 81, u'type': u'duration', u'iteration': 772194}",
            "{u'name': u'AccTrain', u'iteration': 838113, u'subtype': u'train', u'epoch': 88, u'values': {u'accumAccuracy': 71010.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9425897657131479}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 12, u'type': u'duration', u'iteration': 122421}", u'BatchSize: 8',
            "{u'name': u'LossTrain', u'iteration': 348429, u'subtype': u'train', u'epoch': 36, u'values': {u'loss': 0.2378398057317945, "
            "u'accumLoss': "
            "17917.66176480474, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 602688, u'subtype': u'train', u'epoch': 63, u'values': {u'accumAccuracy': 70346.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9337758014203226}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 74, u'type': u'duration', u'iteration': 706275}",
            "{u'name': u'AccDev', u'iteration': 715692, u'subtype': u'evaluation', u'epoch': 75, u'values': {u'accumAccuracy': 4422.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9274328859060402}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 95, u'iteration': 894615}",
            "{u'name': u'CustomMetricDev', u'iteration': 273093, u'subtype': u'evaluation', u'epoch': 28, u'values': {u'truePositives': 55, "
            "u'numExamples': "
            "466, u'micro': {u'recall': 0.3021978021978022, u'precision': 0.16224188790560473, u'f': 0.21113243761996162}, u'macro': {u'recall': "
            "0.13762626262626262, u'precision': 0.07185399221606321, u'f': 0.09441459206660519}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 48, u'2': 0, "
            "u'4': 7}, u'f': {u'1': 0, u'3': 0.2487046632124352, u'2': 0, u'4': 0.11023622047244094}, u'recall': {u'1': 0.0, "
            "u'3': 0.4444444444444444, "
            "u'2': 0.0, u'4': 0.10606060606060606}, u'precision': {u'1': 0, u'3': 0.17266187050359713, u'2': 0, u'4': 0.11475409836065574}, "
            "u'falseNegatives': "
            "{u'1': 4, u'3': 60, u'2': 4, u'4': 59}, u'falsePositives': {u'3': 230, u'4': 54}}, u'falseNegatives': 127, u'beta': 1.0, "
            "u'numLabels': 4, "
            "u'falsePositives': 55}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 659190, u'subtype': u'evaluation', u'epoch': 69, u'values': {u'truePositives': 4411, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9251258389261745, u'precision': 0.9251258389261745, u'f': 0.9251258389261745}, u'macro': {u'recall': "
            "0.5193349296801554, "
            "u'precision': 0.6243835679672538, u'f': 0.5670349776290563}, u'perLabel': {u'truePositives': {u'1': 4, u'0': 4077, u'3': 177, "
            "u'4': 153}, "
            "u'f': {u'1': 0.06451612903225806, u'0': 0.9765269461077845, u'3': 0.5909849749582639, u'2': 0, u'4': 0.8360655737704917}, "
            "u'recall': {u'1': "
            "0.03361344537815126, u'0': 0.9864505202032422, u'3': 0.7797356828193832, u'2': 0.0, u'4': 0.796875}, u'precision': {u'1': 0.8, "
            "u'0': 0.966801043395779, u'3': 0.47580645161290325, u'2': 0, u'4': 0.8793103448275862}, u'falseNegatives': {u'1': 115, u'0': 56, "
            "u'3': 50, "
            "u'2': 97, u'4': 39}, u'falsePositives': {u'1': 1, u'0': 140, u'3': 195, u'4': 21}}, u'falseNegatives': 357, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4411}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 18, u'type': u'duration', u'iteration': 178923}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 58, u'type': u'duration', u'iteration': 555603}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 16, u'type': u'duration', u'iteration': 160089}",
            "{u'name': u'LossTrain', u'iteration': 94170, u'subtype': u'train', u'epoch': 9, u'values': {u'loss': 0.34891677250263664, u'accumLoss': "
            "26285.64505648613, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 649773, u'subtype': u'evaluation', u'epoch': 68, u'values': {u'accumAccuracy': 4404.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9236577181208053}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 583854, u'subtype': u'evaluation', u'epoch': 61, u'values': {u'truePositives': 104, "
            "u'numExamples': "
            "398, u'micro': {u'recall': 0.5714285714285714, u'precision': 0.325, u'f': 0.4143426294820718}, u'macro': {u'recall': "
            "0.2967171717171717, "
            "u'precision': 0.20006787714237229, u'f': 0.23899098732307925}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 66, u'2': 0, u'4': 38}, "
            "u'f': {u'1': 0, u'3': 0.3697478991596639, u'2': 0, u'4': 0.5547445255474452}, u'recall': {u'1': 0.0, u'3': 0.6111111111111112, "
            "u'2': 0.0, "
            "u'4': 0.5757575757575758}, u'precision': {u'1': 0, u'3': 0.26506024096385544, u'2': 0, u'4': 0.5352112676056338}, u'falseNegatives': {"
            "u'1': 4, "
            "u'3': 42, u'2': 4, u'4': 28}, u'falsePositives': {u'3': 183, u'4': 33}}, u'falseNegatives': 78, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': "
            "104}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 743943, u'subtype': u'evaluation', u'epoch': 78, u'values': {u'loss': 0.2018241286277771, "
            "u'accumLoss': "
            "962.2974452972412, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 527352, u'subtype': u'train', u'epoch': 55, u'values': {u'loss': 0.19363718733669977, "
            "u'accumLoss': "
            "14587.657508010278, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 470850, u'subtype': u'evaluation', u'epoch': 49, u'values': {u'truePositives': 4379, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9184144295302014, u'precision': 0.9184144295302014, u'f': 0.9184144295302014}, u'macro': {u'recall': "
            "0.4883823329950937, "
            "u'precision': 0.45094309438533664, u'f': 0.4689165949613805}, u'perLabel': {u'truePositives': {u'0': 4073, u'3': 171, u'4': 135}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9751017476657888, u'3': 0.5560975609756097, u'2': 0, u'4': 0.7692307692307692}, u'recall': {u'1': 0.0, "
            "u'0': 0.9854827002177595, "
            "u'3': 0.7533039647577092, u'2': 0.0, u'4': 0.703125}, u'precision': {u'1': 0, u'0': 0.964937218668562, u'3': 0.44072164948453607, "
            "u'2': 0, "
            "u'4': 0.8490566037735849}, u'falseNegatives': {u'1': 119, u'0': 60, u'3': 56, u'2': 97, u'4': 57}, u'falsePositives': {u'0': 148, "
            "u'3': 217, "
            "u'4': 24}}, u'falseNegatives': 389, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4379}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 593271, u'subtype': u'train', u'epoch': 62, u'values': {u'accumAccuracy': 70320.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.933430676312471}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 404931, u'subtype': u'train', u'epoch': 42, u'values': {u'accumAccuracy': 69559.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.923329129886507}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 34, u'type': u'duration', u'iteration': 329595}",
            "{u'name': u'FMetricDev', u'iteration': 178923, u'subtype': u'evaluation', u'epoch': 18, u'values': {u'truePositives': 4220, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8850671140939598, u'precision': 0.8850671140939598, u'f': 0.8850671140939598}, u'macro': {u'recall': "
            "0.3104108420708932, "
            "u'precision': 0.4266266510527624, u'f': 0.3593563129113565}, u'perLabel': {u'truePositives': {u'0': 4094, u'3': 118, u'4': 8}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9621621621621622, u'3': 0.38752052545155996, u'2': 0, u'4': 0.07960199004975124}, u'recall': {u'1': 0.0, "
            "u'0': 0.9905637551415437, "
            "u'3': 0.5198237885462555, u'2': 0.0, u'4': 0.041666666666666664}, u'precision': {u'1': 0, u'0': 0.9353438428147133, "
            "u'3': 0.3089005235602094, "
            "u'2': 0, u'4': 0.8888888888888888}, u'falseNegatives': {u'1': 119, u'0': 39, u'3': 109, u'2': 97, u'4': 184}, u'falsePositives': {"
            "u'0': 283, "
            "u'3': 264, u'4': 1}}, u'falseNegatives': 548, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4220}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 640356, u'subtype': u'train', u'epoch': 67, u'values': {u'accumAccuracy': 70457.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9352492201499967}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 772194, u'subtype': u'evaluation', u'epoch': 81, u'values': {u'truePositives': 116, "
            "u'numExamples': "
            "441, u'micro': {u'recall': 0.4603174603174603, u'precision': 0.380327868852459, u'f': 0.41651705565529623}, u'macro': {u'recall': "
            "0.33193989443989447, u'precision': 0.31426348008261146, u'f': 0.32285992465458035}, u'perLabel': {u'truePositives': {u'1': 7, "
            "u'3': 71, u'2': 0, "
            "u'4': 38}, u'f': {u'1': 0.15384615384615383, u'3': 0.4409937888198758, u'2': 0, u'4': 0.5428571428571428}, u'recall': {u'1': "
            "0.0945945945945946, "
            "u'3': 0.6574074074074074, u'2': 0.0, u'4': 0.5757575757575758}, u'precision': {u'1': 0.4117647058823529, u'3': 0.3317757009345794, "
            "u'2': 0, "
            "u'4': 0.5135135135135135}, u'falseNegatives': {u'1': 67, u'3': 37, u'2': 4, u'4': 28}, u'falsePositives': {u'1': 10, u'3': 143, "
            "u'4': 36}}, "
            "u'falseNegatives': 136, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 116}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 922866, u'subtype': u'evaluation', u'epoch': 97, u'values': {u'accumAccuracy': 4450.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9333053691275168}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 847530, u'subtype': u'evaluation', u'epoch': 89, u'values': {u'accumAccuracy': 4442.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9316275167785235}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 715692, u'subtype': u'evaluation', u'epoch': 75, u'values': {u'truePositives': 4422, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9274328859060402, u'precision': 0.9274328859060402, u'f': 0.9274328859060403}, u'macro': {u'recall': "
            "0.5308478546245714, "
            "u'precision': 0.6181620829289189, u'f': 0.5711874280770465}, u'perLabel': {u'truePositives': {u'1': 9, u'0': 4080, u'3': 178, "
            "u'4': 155}, "
            "u'f': {u'1': 0.13740458015267173, u'0': 0.9770114942528736, u'3': 0.6054421768707483, u'2': 0, u'4': 0.842391304347826}, "
            "u'recall': {u'1': "
            "0.07563025210084033, u'0': 0.9871763851923542, u'3': 0.7841409691629956, u'2': 0.0, u'4': 0.8072916666666666}, u'precision': {u'1': "
            "0.75, "
            "u'0': 0.9670538042190092, u'3': 0.4930747922437673, u'2': 0, u'4': 0.8806818181818182}, u'falseNegatives': {u'1': 110, u'0': 53, "
            "u'3': 49, "
            "u'2': 97, u'4': 37}, u'falsePositives': {u'1': 3, u'0': 139, u'3': 183, u'4': 21}}, u'falseNegatives': 346, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4422}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 122421, u'subtype': u'evaluation', u'epoch': 12, u'values': {u'truePositives': 4192, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8791946308724832, u'precision': 0.8791946308724832, u'f': 0.8791946308724831}, u'macro': {u'recall': "
            "0.2787552576056532, "
            "u'precision': 0.4605029737197839, u'f': 0.34728764490663494}, u'perLabel': {u'truePositives': {u'1': 1, u'0': 4102, u'3': 88, u'4': 1}, "
            "u'f': {u'1': 0.015384615384615384, u'0': 0.9555089680875845, u'3': 0.3320754716981132, u'2': 0, u'4': 0.010362694300518135}, "
            "u'recall': {u'1': "
            "0.008403361344537815, u'0': 0.9924993951125091, u'3': 0.3876651982378855, u'2': 0.0, u'4': 0.005208333333333333}, u'precision': {u'1': "
            "0.09090909090909091, u'0': 0.9211767347855379, u'3': 0.29042904290429045, u'2': 0, u'4': 1.0}, u'falseNegatives': {u'1': 118, "
            "u'0': 31, u'3': 139, "
            "u'2': 97, u'4': 191}, u'falsePositives': {u'1': 10, u'0': 351, u'3': 215}}, u'falseNegatives': 576, u'beta': 1.0, u'numLabels': 5, "
            "u'falsePositives': 4192}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 357846, u'subtype': u'train', u'epoch': 37, u'values': {u'loss': 0.23509406099761224, "
            "u'accumLoss': "
            "17710.811085255118, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 772194, u'subtype': u'evaluation', u'epoch': 81, u'values': {u'truePositives': 4423, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9276426174496645, u'precision': 0.9276426174496645, u'f': 0.9276426174496645}, u'macro': {u'recall': "
            "0.5386453583062425, "
            "u'precision': 0.5956149454059763, u'f': 0.5656994688622269}, u'perLabel': {u'truePositives': {u'1': 11, u'0': 4074, u'3': 181, "
            "u'4': 157}, "
            "u'f': {u'1': 0.16176470588235295, u'0': 0.9773299748110832, u'3': 0.6104553119730185, u'2': 0, u'4': 0.8418230563002681}, "
            "u'recall': {u'1': "
            "0.09243697478991597, u'0': 0.9857246552141302, u'3': 0.7973568281938326, u'2': 0.0, u'4': 0.8177083333333334}, u'precision': {u'1': "
            "0.6470588235294118, u'0': 0.9690770694576594, u'3': 0.49453551912568305, u'2': 0, u'4': 0.8674033149171271}, u'falseNegatives': {u'1': "
            "108, "
            "u'0': 59, u'3': 46, u'2': 97, u'4': 35}, u'falsePositives': {u'1': 6, u'0': 130, u'3': 185, u'4': 24}}, u'falseNegatives': 345, "
            "u'beta': 1.0, "
            "u'numLabels': 5, u'falsePositives': 4423}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 84753, u'subtype': u'evaluation', u'epoch': 8, u'values': {u'truePositives': 9, "
            "u'numExamples': 414, "
            "u'micro': {u'recall': 0.03571428571428571, u'precision': 0.05263157894736842, u'f': 0.0425531914893617}, u'macro': {u'recall': "
            "0.021896896896896896, u'precision': 0.023573573573573574, u'f': 0.022704322374107737}, u'perLabel': {u'truePositives': {u'1': 1, "
            "u'3': 8, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0.01680672268907563, u'3': 0.0730593607305936, u'2': 0, u'4': 0}, u'recall': {u'1': 0.013513513513513514, "
            "u'3': 0.07407407407407407, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0.022222222222222223, u'3': 0.07207207207207207, u'2': 0, "
            "u'4': 0.0}, "
            "u'falseNegatives': {u'1': 73, u'3': 100, u'2': 4, u'4': 66}, u'falsePositives': {u'1': 44, u'3': 103, u'4': 15}}, u'falseNegatives': "
            "243, "
            "u'beta': 1.0, u'numLabels': 4, u'falsePositives': 9}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 301344, u'subtype': u'train', u'epoch': 31, u'values': {u'loss': 0.25188242473282335, "
            "u'accumLoss': "
            "18975.562467247248, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 310761, u'subtype': u'evaluation', u'epoch': 32, u'values': {u'truePositives': 4336, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9093959731543624, u'precision': 0.9093959731543624, u'f': 0.9093959731543624}, u'macro': {u'recall': "
            "0.4380536019584499, "
            "u'precision': 0.43589891280249377, u'f': 0.43697360123767204}, u'perLabel': {u'truePositives': {u'0': 4081, u'3': 156, u'4': 99}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9716666666666666, u'3': 0.5148514851485148, u'2': 0, u'4': 0.6305732484076433}, u'recall': {u'1': 0.0, "
            "u'0': 0.9874183401887249, "
            "u'3': 0.6872246696035242, u'2': 0.0, u'4': 0.515625}, u'precision': {u'1': 0, u'0': 0.9564096554956644, u'3': 0.41160949868073876, "
            "u'2': 0, "
            "u'4': 0.8114754098360656}, u'falseNegatives': {u'1': 119, u'0': 52, u'3': 71, u'2': 97, u'4': 93}, u'falsePositives': {u'0': 186, "
            "u'3': 223, "
            "u'4': 23}}, u'falseNegatives': 432, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4336}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 83, u'type': u'duration', u'iteration': 791028}",
            "{u'name': u'LossDev', u'iteration': 244842, u'subtype': u'evaluation', u'epoch': 25, u'values': {u'loss': 0.29501470923423767, "
            "u'accumLoss': "
            "1406.6301336288452, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 77, u'type': u'duration', u'iteration': 734526}",
            "{u'name': u'CustomMetricDev', u'iteration': 357846, u'subtype': u'evaluation', u'epoch': 37, u'values': {u'truePositives': 78, "
            "u'numExamples': "
            "451, u'micro': {u'recall': 0.42857142857142855, u'precision': 0.22478386167146974, u'f': 0.2948960302457467}, u'macro': {u'recall': "
            "0.21296296296296297, u'precision': 0.12185905913470621, u'f': 0.15501648388967548}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 56, u'2': 0, "
            "u'4': 22}, u'f': {u'1': 0, u'3': 0.2978723404255319, u'2': 0, u'4': 0.30344827586206896}, u'recall': {u'1': 0.0, "
            "u'3': 0.5185185185185185, "
            "u'2': 0.0, u'4': 0.3333333333333333}, u'precision': {u'1': 0, u'3': 0.208955223880597, u'2': 0, u'4': 0.27848101265822783}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 52, u'2': 4, u'4': 44}, u'falsePositives': {u'3': 212, u'4': 57}}, u'falseNegatives': 104, u'beta': 1.0, u'numLabels': "
            "4, "
            "u'falsePositives': 78}, u'type': u'metric'}",
            u'Reading training examples...',
            "{u'name': u'LossTrain', u'iteration': 621522, u'subtype': u'train', u'epoch': 65, u'values': {u'loss': 0.17772648119063744, "
            "u'accumLoss': "
            "13389.024460496672, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 94, u'iteration': 885198}",
            "{u'name': u'LossTrain', u'iteration': 47085, u'subtype': u'train', u'epoch': 4, u'values': {u'loss': 0.44184030105461286, u'accumLoss': "
            "33286.03907994926, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 207174, u'subtype': u'evaluation', u'epoch': 21, u'values': {u'loss': 0.3051920533180237, "
            "u'accumLoss': "
            "1455.155710220337, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 77, u'iteration': 725109}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 65, u'type': u'duration', u'iteration': 621522}",
            "{u'name': u'AccDev', u'iteration': 28251, u'subtype': u'evaluation', u'epoch': 2, u'values': {u'accumAccuracy': 4133.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8668204697986577}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 546186, u'subtype': u'evaluation', u'epoch': 57, u'values': {u'accumAccuracy': 4399.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9226090604026845}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 395514, u'subtype': u'train', u'epoch': 41, u'values': {u'accumAccuracy': 69519.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9227981681821199}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 301344, u'subtype': u'train', u'epoch': 31, u'values': {u'accumAccuracy': 68900.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.91458153580673}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 546186, u'subtype': u'evaluation', u'epoch': 57, u'values': {u'truePositives': 4399, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9226090604026845, u'precision': 0.9226090604026845, u'f': 0.9226090604026845}, u'macro': {u'recall': "
            "0.5057540111324169, "
            "u'precision': 0.46233112300040186, u'f': 0.483068713038884}, u'perLabel': {u'truePositives': {u'0': 4076, u'3': 174, u'4': 149}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9758199664831217, u'3': 0.5742574257425742, u'2': 0, u'4': 0.8277777777777778}, u'recall': {u'1': 0.0, "
            "u'0': 0.9862085652068715, "
            "u'3': 0.7665198237885462, u'2': 0.0, u'4': 0.7760416666666666}, u'precision': {u'1': 0, u'0': 0.9656479507225776, "
            "u'3': 0.45910290237467016, "
            "u'2': 0, u'4': 0.8869047619047619}, u'falseNegatives': {u'1': 119, u'0': 57, u'3': 53, u'2': 97, u'4': 43}, u'falsePositives': {u'0': "
            "145, "
            "u'3': 205, u'4': 19}}, u'falseNegatives': 369, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4399}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 904032, u'subtype': u'evaluation', u'epoch': 95, u'values': {u'truePositives': 139, "
            "u'numExamples': "
            "480, u'micro': {u'recall': 0.4557377049180328, u'precision': 0.4426751592356688, u'f': 0.4491114701130856}, u'macro': {u'recall': "
            "0.41040562093193667, u'precision': 0.43989911727616643, u'f': 0.4246408664112404}, u'perLabel': {u'truePositives': {u'1': 26, "
            "u'3': 72, u'2': 1, "
            "u'4': 40}, u'f': {u'1': 0.4193548387096775, u'3': 0.4948453608247423, u'2': 0.03333333333333333, u'4': 0.5555555555555556}, "
            "u'recall': {u'1': "
            "0.35135135135135137, u'3': 0.6666666666666666, u'2': 0.017543859649122806, u'4': 0.6060606060606061}, u'precision': {u'1': 0.52, "
            "u'3': 0.39344262295081966, u'2': 0.3333333333333333, u'4': 0.5128205128205128}, u'falseNegatives': {u'1': 48, u'3': 36, u'2': 56, "
            "u'4': 26}, "
            "u'falsePositives': {u'1': 24, u'3': 111, u'2': 2, u'4': 38}}, u'falseNegatives': 166, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 139}, "
            "u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 866364, u'subtype': u'evaluation', u'epoch': 91, u'values': {u'truePositives': 4442, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9316275167785235, u'precision': 0.9316275167785235, u'f': 0.9316275167785235}, u'macro': {u'recall': "
            "0.5680551602757857, "
            "u'precision': 0.6056834794206208, u'f': 0.58626616580957}, u'perLabel': {u'truePositives': {u'1': 25, u'0': 4073, u'3': 183, "
            "u'4': 161}, "
            "u'f': {u'1': 0.32051282051282054, u'0': 0.9779111644657863, u'3': 0.6398601398601399, u'2': 0, u'4': 0.8451443569553806}, "
            "u'recall': {u'1': "
            "0.21008403361344538, u'0': 0.9854827002177595, u'3': 0.8061674008810573, u'2': 0.0, u'4': 0.8385416666666666}, u'precision': {u'1': "
            "0.6756756756756757, u'0': 0.9704550869668811, u'3': 0.5304347826086957, u'2': 0, u'4': 0.8518518518518519}, u'falseNegatives': {u'1': "
            "94, "
            "u'0': 60, u'3': 44, u'2': 97, u'4': 31}, u'falsePositives': {u'1': 12, u'0': 124, u'3': 162, u'4': 28}}, u'falseNegatives': 326, "
            "u'beta': 1.0, "
            "u'numLabels': 5, u'falsePositives': 4442}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 941700, u'subtype': u'evaluation', u'epoch': 99, u'values': {u'accumAccuracy': 4456.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9345637583892618}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 310761, u'subtype': u'evaluation', u'epoch': 32, u'values': {u'truePositives': 74, "
            "u'numExamples': "
            "461, u'micro': {u'recall': 0.4065934065934066, u'precision': 0.2096317280453258, u'f': 0.2766355140186916}, u'macro': {u'recall': "
            "0.1992845117845118, u'precision': 0.11030906403030583, u'f': 0.14201126695106192}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 55, "
            "u'2': 0, "
            "u'4': 19}, u'f': {u'1': 0, u'3': 0.28795811518324604, u'2': 0, u'4': 0.2620689655172414}, u'recall': {u'1': 0.0, "
            "u'3': 0.5092592592592593, "
            "u'2': 0.0, u'4': 0.2878787878787879}, u'precision': {u'1': 0, u'3': 0.20072992700729927, u'2': 0, u'4': 0.24050632911392406}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 53, u'2': 4, u'4': 47}, u'falsePositives': {u'3': 219, u'4': 60}}, u'falseNegatives': 108, u'beta': 1.0, u'numLabels': "
            "4, "
            "u'falsePositives': 74}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 235425, u'subtype': u'evaluation', u'epoch': 24, u'values': {u'truePositives': 4261, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8936661073825504, u'precision': 0.8936661073825504, u'f': 0.8936661073825504}, u'macro': {u'recall': "
            "0.35906631640927417, "
            "u'precision': 0.42938840575746806, u'f': 0.39109135586248445}, u'perLabel': {u'truePositives': {u'0': 4083, u'3': 149, u'4': 29}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9681090693538826, u'3': 0.4522003034901365, u'2': 0, u'4': 0.25663716814159293}, u'recall': {u'1': 0.0, "
            "u'0': 0.9879022501814663, "
            "u'3': 0.6563876651982379, u'2': 0.0, u'4': 0.15104166666666666}, u'precision': {u'1': 0, u'0': 0.9490934449093444, "
            "u'3': 0.3449074074074074, "
            "u'2': 0, u'4': 0.8529411764705882}, u'falseNegatives': {u'1': 119, u'0': 50, u'3': 78, u'2': 97, u'4': 163}, u'falsePositives': {u'0': "
            "219, "
            "u'3': 283, u'4': 5}}, u'falseNegatives': 507, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4261}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 254259, u'subtype': u'evaluation', u'epoch': 26, u'values': {u'truePositives': 45, "
            "u'numExamples': "
            "468, u'micro': {u'recall': 0.24725274725274726, u'precision': 0.13595166163141995, u'f': 0.1754385964912281}, u'macro': {u'recall': "
            "0.10563973063973063, u'precision': 0.04418767507002801, u'f': 0.06231135178348299}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 44, u'2': 0, "
            "u'4': 1}, u'f': {u'1': 0, u'3': 0.22680412371134023, u'2': 0, u'4': 0.017094017094017096}, u'recall': {u'1': 0.0, "
            "u'3': 0.4074074074074074, "
            "u'2': 0.0, u'4': 0.015151515151515152}, u'precision': {u'1': 0, u'3': 0.15714285714285714, u'2': 0, u'4': 0.0196078431372549}, "
            "u'falseNegatives': "
            "{u'1': 4, u'3': 64, u'2': 4, u'4': 65}, u'falsePositives': {u'3': 236, u'4': 50}}, u'falseNegatives': 137, u'beta': 1.0, "
            "u'numLabels': 4, "
            "u'falsePositives': 45}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 499101, u'subtype': u'train', u'epoch': 52, u'values': {u'accumAccuracy': 70004.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9292360788478131}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 15, u'type': u'duration', u'iteration': 150672}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 82, u'type': u'duration', u'iteration': 781611}",
            "{u'name': u'LossTrain', u'iteration': 310761, u'subtype': u'train', u'epoch': 32, u'values': {u'loss': 0.24914386037613137, "
            "u'accumLoss': "
            "18769.252721435856, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 53, u'iteration': 499101}",
            "{u'name': u'FMetricDev', u'iteration': 508518, u'subtype': u'evaluation', u'epoch': 53, u'values': {u'truePositives': 4389, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.920511744966443, u'precision': 0.920511744966443, u'f': 0.920511744966443}, u'macro': {u'recall': "
            "0.49367201192685356, "
            "u'precision': 0.45928892164876683, u'f': 0.47586019115246214}, u'perLabel': {u'truePositives': {u'0': 4078, u'3': 172, u'4': 139}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9752481167045318, u'3': 0.5667215815485996, u'2': 0, u'4': 0.7942857142857144}, u'recall': {u'1': 0.0, "
            "u'0': 0.9866924751996129, "
            "u'3': 0.7577092511013216, u'2': 0.0, u'4': 0.7239583333333334}, u'precision': {u'1': 0, u'0': 0.9640661938534278, "
            "u'3': 0.45263157894736844, "
            "u'2': 0, u'4': 0.879746835443038}, u'falseNegatives': {u'1': 119, u'0': 55, u'3': 55, u'2': 97, u'4': 53}, u'falsePositives': {u'0': "
            "152, "
            "u'3': 208, u'4': 19}}, u'falseNegatives': 379, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4389}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 480267, u'subtype': u'evaluation', u'epoch': 50, u'values': {u'accumAccuracy': 4381.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9188338926174496}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 263676, u'subtype': u'evaluation', u'epoch': 27, u'values': {u'truePositives': 4288, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8993288590604027, u'precision': 0.8993288590604027, u'f': 0.8993288590604027}, u'macro': {u'recall': "
            "0.3833788231376482, "
            "u'precision': 0.43507961980206844, u'f': 0.4075962904403152}, u'perLabel': {u'truePositives': {u'0': 4087, u'3': 148, u'4': 53}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9683686766970739, u'3': 0.47359999999999997, u'2': 0, u'4': 0.4173228346456693}, u'recall': {u'1': 0.0, "
            "u'0': 0.988870070166949, "
            "u'3': 0.6519823788546255, u'2': 0.0, u'4': 0.2760416666666667}, u'precision': {u'1': 0, u'0': 0.9487000928505107, "
            "u'3': 0.37185929648241206, "
            "u'2': 0, u'4': 0.8548387096774194}, u'falseNegatives': {u'1': 119, u'0': 46, u'3': 79, u'2': 97, u'4': 139}, u'falsePositives': {u'0': "
            "221, "
            "u'3': 250, u'4': 9}}, u'falseNegatives': 480, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4288}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 376680, u'subtype': u'train', u'epoch': 39, u'values': {u'accumAccuracy': 69428.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9215902303046393}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 67, u'type': u'duration', u'iteration': 640356}",
            "{u'name': u'CustomMetricDev', u'iteration': 178923, u'subtype': u'evaluation', u'epoch': 18, u'values': {u'truePositives': 35, "
            "u'numExamples': "
            "400, u'micro': {u'recall': 0.19230769230769232, u'precision': 0.1383399209486166, u'f': 0.16091954022988506}, u'macro': {u'recall': "
            "0.08101851851851852, u'precision': 0.035860655737704916, u'f': 0.04971590909090909}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 35, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0, u'3': 0.19886363636363635, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.32407407407407407, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0.14344262295081966, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 4, u'3': 73, u'2': 4, u'4': 66}, "
            "u'falsePositives': {u'3': 209, u'4': 9}}, u'falseNegatives': 147, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 35}, "
            "u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 80, u'type': u'duration', u'iteration': 762777}",
            "{u'name': u'LossDev', u'iteration': 273093, u'subtype': u'evaluation', u'epoch': 28, u'values': {u'loss': 0.28677812218666077, "
            "u'accumLoss': "
            "1367.3580865859985, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 87, u'iteration': 819279}",
            "{u'name': u'AccTrain', u'iteration': 273093, u'subtype': u'train', u'epoch': 28, u'values': {u'accumAccuracy': 68452.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9086347647175947}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 54, u'iteration': 508518}",
            "{u'name': u'AccTrain', u'iteration': 188340, u'subtype': u'train', u'epoch': 19, u'values': {u'accumAccuracy': 67455.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.895400544235747}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 574437, u'subtype': u'evaluation', u'epoch': 60, u'values': {u'truePositives': 4401, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9230285234899329, u'precision': 0.9230285234899329, u'f': 0.9230285234899329}, u'macro': {u'recall': "
            "0.5075161256698618, "
            "u'precision': 0.465493869723545, u'f': 0.4855975712554654}, u'perLabel': {u'truePositives': {u'0': 4076, u'3': 176, u'4': 149}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9760536398467432, u'3': 0.5761047463175123, u'2': 0, u'4': 0.8347338935574229}, u'recall': {u'1': 0.0, "
            "u'0': 0.9862085652068715, "
            "u'3': 0.775330396475771, u'2': 0.0, u'4': 0.7760416666666666}, u'precision': {u'1': 0, u'0': 0.9661057122540887, "
            "u'3': 0.4583333333333333, "
            "u'2': 0, u'4': 0.9030303030303031}, u'falseNegatives': {u'1': 119, u'0': 57, u'3': 51, u'2': 97, u'4': 43}, u'falsePositives': {u'0': "
            "143, "
            "u'3': 208, u'4': 16}}, u'falseNegatives': 367, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4401}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 508518, u'subtype': u'train', u'epoch': 53, u'values': {u'accumAccuracy': 70040.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9297139443817615}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 781611, u'subtype': u'evaluation', u'epoch': 82, u'values': {u'loss': 0.1991714984178543, "
            "u'accumLoss': "
            "949.6497044563293, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 809862, u'subtype': u'train', u'epoch': 85, u'values': {u'loss': 0.1563296334615911, "
            "u'accumLoss': "
            "11777.092936828965, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 282510, u'subtype': u'evaluation', u'epoch': 29, u'values': {u'truePositives': 60, "
            "u'numExamples': "
            "471, u'micro': {u'recall': 0.32967032967032966, u'precision': 0.17191977077363896, u'f': 0.2259887005649717}, u'macro': {u'recall': "
            "0.15361952861952863, u'precision': 0.0812486916474775, u'f': 0.10628415966749069}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 50, "
            "u'2': 0, "
            "u'4': 10}, u'f': {u'1': 0, u'3': 0.25706940874035994, u'2': 0, u'4': 0.14925373134328357}, u'recall': {u'1': 0.0, "
            "u'3': 0.46296296296296297, "
            "u'2': 0.0, u'4': 0.15151515151515152}, u'precision': {u'1': 0, u'3': 0.17793594306049823, u'2': 0, u'4': 0.14705882352941177}, "
            "u'falseNegatives': "
            "{u'1': 4, u'3': 58, u'2': 4, u'4': 56}, u'falsePositives': {u'3': 231, u'4': 58}}, u'falseNegatives': 122, u'beta': 1.0, "
            "u'numLabels': 4, "
            "u'falsePositives': 60}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 21, u'type': u'duration', u'iteration': 207174}",
            "{u'name': u'LossTrain', u'iteration': 386097, u'subtype': u'train', u'epoch': 40, u'values': {u'loss': 0.226970161775772, u'accumLoss': "
            "17098.797137377784, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 376680, u'subtype': u'evaluation', u'epoch': 39, u'values': {u'truePositives': 4357, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9138003355704698, u'precision': 0.9138003355704698, u'f': 0.9138003355704698}, u'macro': {u'recall': "
            "0.46194477257296224, "
            "u'precision': 0.4403009555211628, u'f': 0.45086325915119824}, u'perLabel': {u'truePositives': {u'0': 4078, u'3': 162, u'4': 117}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9733858455662967, u'3': 0.5355371900826446, u'2': 0, u'4': 0.6964285714285714}, u'recall': {u'1': 0.0, "
            "u'0': 0.9866924751996129, "
            "u'3': 0.7136563876651982, u'2': 0.0, u'4': 0.609375}, u'precision': {u'1': 0, u'0': 0.9604333490343853, u'3': 0.42857142857142855, "
            "u'2': 0, "
            "u'4': 0.8125}, u'falseNegatives': {u'1': 119, u'0': 55, u'3': 65, u'2': 97, u'4': 75}, u'falsePositives': {u'0': 168, u'3': 216, "
            "u'4': 27}}, "
            "u'falseNegatives': 411, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4357}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 44, u'type': u'duration', u'iteration': 423765}",
            "{u'name': u'AccDev', u'iteration': 150672, u'subtype': u'evaluation', u'epoch': 15, u'values': {u'accumAccuracy': 4199.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8806627516778524}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 113004, u'subtype': u'evaluation', u'epoch': 11, u'values': {u'truePositives': 23, "
            "u'numExamples': "
            "387, u'micro': {u'recall': 0.12105263157894737, u'precision': 0.10454545454545454, u'f': 0.1121951219512195}, u'macro': {u'recall': "
            "0.0543043043043043, u'precision': 0.03878834694327963, u'f': 0.04525328621841042}, u'perLabel': {u'truePositives': {u'1': 1, u'3': 22, "
            "u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0.020618556701030927, u'3': 0.1442622950819672, u'2': 0, u'4': 0}, u'recall': {u'1': 0.013513513513513514, "
            "u'3': 0.2037037037037037, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0.043478260869565216, u'3': 0.1116751269035533, u'2': 0, "
            "u'4': 0}, "
            "u'falseNegatives': {u'1': 73, u'3': 86, u'2': 4, u'4': 4}, u'falsePositives': {u'1': 22, u'3': 175}}, u'falseNegatives': 167, "
            "u'beta': 1.0, "
            "u'numLabels': 4, u'falsePositives': 23}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 630939, u'subtype': u'evaluation', u'epoch': 66, u'values': {u'loss': 0.21265383064746857, "
            "u'accumLoss': "
            "1013.9334645271301, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 819279, u'subtype': u'evaluation', u'epoch': 86, u'values': {u'truePositives': 124, "
            "u'numExamples': "
            "504, u'micro': {u'recall': 0.4065573770491803, u'precision': 0.38390092879256965, u'f': 0.3949044585987261}, u'macro': {u'recall': "
            "0.35913185913185913, u'precision': 0.3236020372321742, u'f': 0.34044245311084315}, u'perLabel': {u'truePositives': {u'1': 11, "
            "u'3': 72, u'2': 0, "
            "u'4': 41}, u'f': {u'1': 0.2222222222222222, u'3': 0.44036697247706424, u'2': 0, u'4': 0.5694444444444445}, u'recall': {u'1': "
            "0.14864864864864866, "
            "u'3': 0.6666666666666666, u'2': 0.0, u'4': 0.6212121212121212}, u'precision': {u'1': 0.44, u'3': 0.3287671232876712, u'2': 0.0, "
            "u'4': 0.5256410256410257}, u'falseNegatives': {u'1': 63, u'3': 36, u'2': 57, u'4': 25}, u'falsePositives': {u'1': 14, u'3': 147, "
            "u'2': 1, "
            "u'4': 37}}, u'falseNegatives': 181, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 124}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 50, u'iteration': 470850}",
            "{u'name': u'LossTrain', u'iteration': 423765, u'subtype': u'train', u'epoch': 44, u'values': {u'loss': 0.21687377688330375, "
            "u'accumLoss': "
            "16338.185981503688, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 207174, u'subtype': u'evaluation', u'epoch': 21, u'values': {u'truePositives': 4237, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8886325503355704, u'precision': 0.8886325503355704, u'f': 0.8886325503355704}, u'macro': {u'recall': "
            "0.33317441158037114, "
            "u'precision': 0.43059625002203195, u'f': 0.375672068704016}, u'perLabel': {u'truePositives': {u'0': 4086, u'3': 136, u'4': 15}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9648170011806375, u'3': 0.4243369734789392, u'2': 0, u'4': 0.14354066985645936}, u'recall': {u'1': 0.0, "
            "u'0': 0.9886281151705782, "
            "u'3': 0.5991189427312775, u'2': 0.0, u'4': 0.078125}, u'precision': {u'1': 0, u'0': 0.9421258934747522, u'3': 0.3285024154589372, "
            "u'2': 0, "
            "u'4': 0.8823529411764706}, u'falseNegatives': {u'1': 119, u'0': 47, u'3': 91, u'2': 97, u'4': 177}, u'falsePositives': {u'0': 251, "
            "u'3': 278, "
            "u'4': 2}}, u'falseNegatives': 531, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4237}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 555603, u'subtype': u'evaluation', u'epoch': 58, u'values': {u'accumAccuracy': 4400.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9228187919463087}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 122421, u'subtype': u'evaluation', u'epoch': 12, u'values': {u'loss': 0.33743682503700256, "
            "u'accumLoss': "
            "1608.8987817764282, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 47085, u'subtype': u'evaluation', u'epoch': 4, u'values': {u'truePositives': 0, "
            "u'numExamples': 233, "
            "u'micro': {u'recall': 0.0, u'precision': 0.0, u'f': 0}, u'macro': {u'recall': 0.0, u'precision': 0.0, u'f': 0}, u'perLabel': {"
            "u'truePositives': {"
            "u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'f': {u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.0, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0.0, u'3': 0.0, u'2': 0, u'4': 0}, u'falseNegatives': {u'1': 74, u'3': 108, u'2': 4, u'4': 4}, u'falsePositives': "
            "{u'1': 22, "
            "u'3': 21}}, u'falseNegatives': 190, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 0}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 725109, u'subtype': u'train', u'epoch': 76, u'values': {u'accumAccuracy': 70698.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9384482644189288}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 99, u'type': u'duration', u'iteration': 941700}",
            "{u'name': u'LossTrain', u'iteration': 696858, u'subtype': u'train', u'epoch': 73, u'values': {u'loss': 0.16786441384254924, "
            "u'accumLoss': "
            "12646.065616828448, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 235425, u'subtype': u'evaluation', u'epoch': 24, u'values': {u'accumAccuracy': 4261.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8936661073825504}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 55, u'iteration': 517935}",
            "{u'name': u'AccTrain', u'iteration': 828696, u'subtype': u'train', u'epoch': 87, u'values': {u'accumAccuracy': 71012.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9426163137983673}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 659190, u'subtype': u'evaluation', u'epoch': 69, u'values': {u'truePositives': 110, "
            "u'numExamples': "
            "456, u'micro': {u'recall': 0.4365079365079365, u'precision': 0.3503184713375796, u'f': 0.3886925795053004}, u'macro': {u'recall': "
            "0.31338725088725083, u'precision': 0.3998055491061064, u'f': 0.3513607033750129}, u'perLabel': {u'truePositives': {u'1': 4, u'3': 69, "
            "u'2': 0, "
            "u'4': 37}, u'f': {u'1': 0.10126582278481013, u'3': 0.4011627906976744, u'2': 0, u'4': 0.5323741007194245}, u'recall': {u'1': "
            "0.05405405405405406, "
            "u'3': 0.6388888888888888, u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 0.8, u'3': 0.2923728813559322, u'2': 0, "
            "u'4': 0.5068493150684932}, u'falseNegatives': {u'1': 70, u'3': 39, u'2': 4, u'4': 29}, u'falsePositives': {u'1': 1, u'3': 167, "
            "u'4': 36}}, "
            "u'falseNegatives': 142, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 110}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 47085, u'subtype': u'evaluation', u'epoch': 4, u'values': {u'truePositives': 4132, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8666107382550335, u'precision': 0.8666107382550335, u'f': 0.8666107382550335}, u'macro': {u'recall': "
            "0.19995160900072587, "
            "u'precision': 0.17489947089947092, u'f': 0.18658839467148342}, u'perLabel': {u'truePositives': {u'0': 4132}, u'f': {u'1': 0, "
            "u'0': 0.932941973357417, u'3': 0, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'0': 0.9997580450036293, u'3': 0.0, u'2': 0.0, u'4': 0.0}, "
            "u'precision': {u'1': 0.0, u'0': 0.8744973544973546, u'3': 0.0, u'2': 0, u'4': 0}, u'falseNegatives': {u'1': 119, u'0': 1, u'3': 227, "
            "u'2': 97, "
            "u'4': 192}, u'falsePositives': {u'1': 22, u'0': 593, u'3': 21}}, u'falseNegatives': 636, u'beta': 1.0, u'numLabels': 5, "
            "u'falsePositives': 4132}, "
            "u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 546186, u'subtype': u'train', u'epoch': 57, u'values': {u'loss': 0.19009349827168723, "
            "u'accumLoss': "
            "14320.693692297558, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 838113, u'subtype': u'evaluation', u'epoch': 88, u'values': {u'truePositives': 128, "
            "u'numExamples': "
            "426, u'micro': {u'recall': 0.5079365079365079, u'precision': 0.423841059602649, u'f': 0.4620938628158845}, u'macro': {u'recall': "
            "0.3750170625170625, u'precision': 0.35255624572495514, u'f': 0.36343996170853726}, u'perLabel': {u'truePositives': {u'1': 20, "
            "u'3': 69, u'2': 0, "
            "u'4': 39}, u'f': {u'1': 0.35398230088495575, u'3': 0.46308724832214765, u'2': 0, u'4': 0.5611510791366907}, u'recall': {u'1': "
            "0.2702702702702703, "
            "u'3': 0.6388888888888888, u'2': 0.0, u'4': 0.5909090909090909}, u'precision': {u'1': 0.5128205128205128, u'3': 0.3631578947368421, "
            "u'2': 0, "
            "u'4': 0.5342465753424658}, u'falseNegatives': {u'1': 54, u'3': 39, u'2': 4, u'4': 27}, u'falsePositives': {u'1': 19, u'3': 121, "
            "u'4': 34}}, "
            "u'falseNegatives': 124, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 128}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 659190, u'subtype': u'evaluation', u'epoch': 69, u'values': {u'accumAccuracy': 4411.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9251258389261745}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 83, u'iteration': 781611}", "{u'learn_rate': [0.001], u'epoch': 45, u'iteration': 423765}",
            "{u'name': u'LossDev', u'iteration': 649773, u'subtype': u'evaluation', u'epoch': 68, u'values': {u'loss': 0.21003572642803192, "
            "u'accumLoss': "
            "1001.4503436088562, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 244842, u'subtype': u'evaluation', u'epoch': 25, u'values': {u'truePositives': 4282, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8980704697986577, u'precision': 0.8980704697986577, u'f': 0.8980704697986577}, u'macro': {u'recall': "
            "0.37994804074188165, "
            "u'precision': 0.4320052455379052, u'f': 0.4043078571290678}, u'perLabel': {u'truePositives': {u'0': 4084, u'3': 149, u'4': 49}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9682313892840207, u'3': 0.4700315457413249, u'2': 0, u'4': 0.392}, u'recall': {u'1': 0.0, u'0': 0.988144205177837, "
            "u'3': 0.6563876651982379, u'2': 0.0, u'4': 0.2552083333333333}, u'precision': {u'1': 0, u'0': 0.9491052753892633, "
            "u'3': 0.36609336609336607, "
            "u'2': 0, u'4': 0.8448275862068966}, u'falseNegatives': {u'1': 119, u'0': 49, u'3': 78, u'2': 97, u'4': 143}, u'falsePositives': {u'0': "
            "219, "
            "u'3': 258, u'4': 9}}, u'falseNegatives': 486, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4282}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 621522, u'subtype': u'evaluation', u'epoch': 65, u'values': {u'truePositives': 4408, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.924496644295302, u'precision': 0.924496644295302, u'f': 0.924496644295302}, u'macro': {u'recall': "
            "0.5061564788566209, "
            "u'precision': 0.5671562278269839, u'f': 0.5349229492037182}, u'perLabel': {u'truePositives': {u'1': 1, u'0': 4086, u'3': 172, "
            "u'4': 149}, "
            "u'f': {u'1': 0.01652892561983471, u'0': 0.9763440860215054, u'3': 0.5830508474576271, u'2': 0, u'4': 0.8324022346368715}, "
            "u'recall': {u'1': "
            "0.008403361344537815, u'0': 0.9886281151705782, u'3': 0.7577092511013216, u'2': 0.0, u'4': 0.7760416666666666}, u'precision': {u'1': "
            "0.5, "
            "u'0': 0.9643615765872079, u'3': 0.4738292011019284, u'2': 0, u'4': 0.8975903614457831}, u'falseNegatives': {u'1': 118, u'0': 47, "
            "u'3': 55, "
            "u'2': 97, u'4': 43}, u'falsePositives': {u'1': 1, u'0': 151, u'3': 191, u'4': 17}}, u'falseNegatives': 360, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4408}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 41, u'type': u'duration', u'iteration': 395514}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 19, u'type': u'duration', u'iteration': 188340}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 59, u'type': u'duration', u'iteration': 565020}",
            "{u'name': u'LossTrain', u'iteration': 725109, u'subtype': u'train', u'epoch': 76, u'values': {u'loss': 0.1647307786999174, "
            "u'accumLoss': "
            "12409.993213358277, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 197757, u'subtype': u'train', u'epoch': 20, u'values': {u'accumAccuracy': 67567.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.8968872370080307}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 56502, u'subtype': u'evaluation', u'epoch': 5, u'values': {u'accumAccuracy': 4139.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8680788590604027}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 809862, u'subtype': u'evaluation', u'epoch': 85, u'values': {u'loss': 0.19732894003391266, "
            "u'accumLoss': "
            "940.8643860816956, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 22, u'type': u'duration', u'iteration': 216591}",
            "{u'name': u'FMetricDev', u'iteration': 791028, u'subtype': u'evaluation', u'epoch': 83, u'values': {u'truePositives': 4432, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9295302013422819, u'precision': 0.9295302013422819, u'f': 0.9295302013422819}, u'macro': {u'recall': "
            "0.5549583450610104, "
            "u'precision': 0.5994125266182849, u'f': 0.5763294829104766}, u'perLabel': {u'truePositives': {u'1': 19, u'0': 4072, u'3': 182, "
            "u'4': 159}, "
            "u'f': {u'1': 0.25675675675675674, u'0': 0.9774363898223716, u'3': 0.6254295532646048, u'2': 0, u'4': 0.8435013262599469}, "
            "u'recall': {u'1': "
            "0.15966386554621848, u'0': 0.9852407452213888, u'3': 0.801762114537445, u'2': 0.0, u'4': 0.828125}, u'precision': {u'1': "
            "0.6551724137931034, "
            "u'0': 0.9697547035008335, u'3': 0.5126760563380282, u'2': 0, u'4': 0.8594594594594595}, u'falseNegatives': {u'1': 100, u'0': 61, "
            "u'3': 45, "
            "u'2': 97, u'4': 33}, u'falsePositives': {u'1': 10, u'0': 127, u'3': 173, u'4': 26}}, u'falseNegatives': 336, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4432}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 24, u'iteration': 226008}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 63, u'type': u'duration', u'iteration': 602688}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 42, u'type': u'duration', u'iteration': 404931}",
            "{u'name': u'AccTrain', u'iteration': 226008, u'subtype': u'train', u'epoch': 23, u'values': {u'accumAccuracy': 67923.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9016127961770757}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 640356, u'subtype': u'evaluation', u'epoch': 67, u'values': {u'loss': 0.21083296835422516, "
            "u'accumLoss': "
            "1005.2515931129456, u'numExamples': 4768}, u'type': u'metric'}",
            u'Loading char lexicon...',
            "{u'name': u'CustomMetricDev', u'iteration': 169506, u'subtype': u'evaluation', u'epoch': 17, u'values': {u'truePositives': 30, "
            "u'numExamples': "
            "385, u'micro': {u'recall': 0.16483516483516483, u'precision': 0.12875536480686695, u'f': 0.14457831325301201}, u'macro': {u'recall': "
            "0.06944444444444445, u'precision': 0.03275109170305677, u'f': 0.04451038575667656}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 30, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0, u'3': 0.17804154302670624, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.2777777777777778, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0.13100436681222707, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 4, u'3': 78, u'2': 4, u'4': 66}, "
            "u'falsePositives': {u'3': 199, u'4': 4}}, u'falseNegatives': 152, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 30}, "
            "u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 781611, u'subtype': u'train', u'epoch': 82, u'values': {u'accumAccuracy': 70855.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9405322891086481}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 12, u'iteration': 113004}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 24, u'type': u'duration', u'iteration': 235425}",
            "{u'learn_rate': [0.001], u'epoch': 0, u'iteration': 0}", "{u'learn_rate': [0.001], u'epoch': 9, u'iteration': 84753}",
            "{u'name': u'AccTrain', u'iteration': 678024, u'subtype': u'train', u'epoch': 71, u'values': {u'accumAccuracy': 70573.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9367890090927192}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 668607, u'subtype': u'evaluation', u'epoch': 70, u'values': {u'loss': 0.2077799290418625, "
            "u'accumLoss': "
            "990.6947016716003, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 188340, u'subtype': u'evaluation', u'epoch': 19, u'values': {u'accumAccuracy': 4221.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8852768456375839}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 499101, u'subtype': u'evaluation', u'epoch': 52, u'values': {u'truePositives': 4386, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9198825503355704, u'precision': 0.9198825503355704, u'f': 0.9198825503355704}, u'macro': {u'recall': "
            "0.49769017027627277, "
            "u'precision': 0.45434804631162506, u'f': 0.475032519900208}, u'perLabel': {u'truePositives': {u'0': 4070, u'3': 177, u'4': 139}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9756682248591633, u'3': 0.5682182985553773, u'2': 0, u'4': 0.7853107344632769}, u'recall': {u'1': 0.0, "
            "u'0': 0.9847568352286474, "
            "u'3': 0.7797356828193832, u'2': 0.0, u'4': 0.7239583333333334}, u'precision': {u'1': 0, u'0': 0.9667458432304038, "
            "u'3': 0.44696969696969696, "
            "u'2': 0, u'4': 0.8580246913580247}, u'falseNegatives': {u'1': 119, u'0': 63, u'3': 50, u'2': 97, u'4': 53}, u'falsePositives': {u'0': "
            "140, "
            "u'3': 219, u'4': 23}}, u'falseNegatives': 382, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4386}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 574437, u'subtype': u'evaluation', u'epoch': 60, u'values': {u'accumAccuracy': 4401.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9230285234899329}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 913449, u'subtype': u'evaluation', u'epoch': 96, u'values': {u'loss': 0.19086198508739471, "
            "u'accumLoss': "
            "910.029944896698, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 207174, u'subtype': u'evaluation', u'epoch': 21, u'values': {u'accumAccuracy': 4237.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8886325503355704}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 7, u'iteration': 65919}",
            "{u'name': u'LossTrain', u'iteration': 668607, u'subtype': u'train', u'epoch': 70, u'values': {u'loss': 0.17131287220346358, "
            "u'accumLoss': "
            "12905.85522744793, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 69, u'iteration': 649773}",
            "{u'name': u'AccDev', u'iteration': 395514, u'subtype': u'evaluation', u'epoch': 41, u'values': {u'accumAccuracy': 4361.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9146392617449665}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 84, u'type': u'duration', u'iteration': 800445}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 59, u'type': u'duration', u'iteration': 565020}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 39, u'type': u'duration', u'iteration': 376680}",
            "{u'name': u'AccDev', u'iteration': 470850, u'subtype': u'evaluation', u'epoch': 49, u'values': {u'accumAccuracy': 4379.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9184144295302014}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 82, u'type': u'duration', u'iteration': 781611}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 51, u'type': u'duration', u'iteration': 489684}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 35, u'type': u'duration', u'iteration': 339012}",
            "{u'name': u'LossDev', u'iteration': 56502, u'subtype': u'evaluation', u'epoch': 5, u'values': {u'loss': 0.41335615515708923, "
            "u'accumLoss': "
            "1970.8821477890015, u'numExamples': 4768}, u'type': u'metric'}",
            u'Loading word filters...', "{u'duration': 7, u'subtype': u'training', u'epoch': 19, u'type': u'duration', u'iteration': 188340}",
            "{u'name': u'AccTrain', u'iteration': 517935, u'subtype': u'train', u'epoch': 54, u'values': {u'accumAccuracy': 70065.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9300457954470034}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 29, u'type': u'duration', u'iteration': 282510}",
            "{u'learn_rate': [0.001], u'epoch': 25, u'iteration': 235425}",
            "{u'name': u'AccTrain', u'iteration': 442599, u'subtype': u'train', u'epoch': 46, u'values': {u'accumAccuracy': 69728.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9255724430875423}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 386097, u'subtype': u'train', u'epoch': 40, u'values': {u'accumAccuracy': 69487.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9223733988186102}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 71, u'type': u'duration', u'iteration': 678024}",
            "{u'name': u'LossTrain', u'iteration': 574437, u'subtype': u'train', u'epoch': 60, u'values': {u'loss': 0.18509045260534002, "
            "u'accumLoss': "
            "13943.789247023291, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 489684, u'subtype': u'evaluation', u'epoch': 51, u'values': {u'accumAccuracy': 4384.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9194630872483222}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 89, u'type': u'duration', u'iteration': 847530}",
            "{u'learn_rate': [0.001], u'epoch': 52, u'iteration': 489684}",
            "{u'name': u'AccTrain', u'iteration': 772194, u'subtype': u'train', u'epoch': 81, u'values': {u'accumAccuracy': 70859.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9405853852790867}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 15, u'iteration': 141255}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 50, u'type': u'duration', u'iteration': 480267}",
            "{u'name': u'AccDev', u'iteration': 630939, u'subtype': u'evaluation', u'epoch': 66, u'values': {u'accumAccuracy': 4401.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9230285234899329}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 113004, u'subtype': u'train', u'epoch': 11, u'values': {u'loss': 0.3306419169321966, "
            "u'accumLoss': "
            "24908.90881208703, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 14, u'subtype': u'training', u'epoch': 2, u'type': u'duration', u'iteration': 28251}",
            "{u'name': u'CustomMetricDev', u'iteration': 235425, u'subtype': u'evaluation', u'epoch': 24, u'values': {u'truePositives': 47, "
            "u'numExamples': "
            "451, u'micro': {u'recall': 0.25824175824175827, u'precision': 0.14873417721518986, u'f': 0.18875502008032127}, u'macro': {u'recall': "
            "0.1087962962962963, u'precision': 0.0412280701754386, u'f': 0.05979643765903308}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 47, "
            "u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0, u'3': 0.23918575063613232, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.4351851851851852, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0.1649122807017544, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 4, u'3': 61, u'2': 4, u'4': 66}, "
            "u'falsePositives': {u'3': 238, u'4': 31}}, u'falseNegatives': 135, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 47}, "
            "u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 19, u'iteration': 178923}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 91, u'type': u'duration', u'iteration': 866364}",
            "{u'name': u'AccTrain', u'iteration': 480267, u'subtype': u'train', u'epoch': 50, u'values': {u'accumAccuracy': 69908.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9279617707572841}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 47085, u'subtype': u'evaluation', u'epoch': 4, u'values': {u'accumAccuracy': 4132.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8666107382550335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 470850, u'subtype': u'evaluation', u'epoch': 49, u'values': {u'truePositives': 95, "
            "u'numExamples': "
            "430, u'micro': {u'recall': 0.521978021978022, u'precision': 0.27696793002915454, u'f': 0.3619047619047619}, u'macro': {u'recall': "
            "0.2670454545454546, u'precision': 0.15988593155893538, u'f': 0.2000172049104839}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 63, "
            "u'2': 0, "
            "u'4': 32}, u'f': {u'1': 0, u'3': 0.33962264150943394, u'2': 0, u'4': 0.4383561643835617}, u'recall': {u'1': 0.0, "
            "u'3': 0.5833333333333334, "
            "u'2': 0.0, u'4': 0.48484848484848486}, u'precision': {u'1': 0, u'3': 0.23954372623574144, u'2': 0, u'4': 0.4}, u'falseNegatives': {"
            "u'1': 4, "
            "u'3': 45, u'2': 4, u'4': 34}, u'falsePositives': {u'3': 200, u'4': 48}}, u'falseNegatives': 87, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': "
            "95}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 565020, u'subtype': u'train', u'epoch': 59, u'values': {u'loss': 0.18667005411975054, "
            "u'accumLoss': "
            "14062.788527111406, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 3, u'type': u'duration', u'iteration': 37668}",
            "{u'name': u'AccDev', u'iteration': 565020, u'subtype': u'evaluation', u'epoch': 59, u'values': {u'accumAccuracy': 4400.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9228187919463087}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 630939, u'subtype': u'train', u'epoch': 66, u'values': {u'loss': 0.17640004574849766, "
            "u'accumLoss': "
            "13289.09744646307, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 527352, u'subtype': u'train', u'epoch': 55, u'values': {u'accumAccuracy': 70109.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9306298533218291}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 73, u'type': u'duration', u'iteration': 696858}",
            "{u'name': u'FMetricDev', u'iteration': 56502, u'subtype': u'evaluation', u'epoch': 5, u'values': {u'truePositives': 4139, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8680788590604027, u'precision': 0.8680788590604027, u'f': 0.8680788590604027}, u'macro': {u'recall': "
            "0.20973784248620167, "
            "u'precision': 0.42347916250770956, u'f': 0.280534493488799}, u'perLabel': {u'truePositives': {u'1': 1, u'0': 4129, u'3': 7, u'4': 2}, "
            "u'f': {u'1': 0.012658227848101267, u'0': 0.9355386881160078, u'3': 0.05384615384615384, u'2': 0, u'4': 0.020618556701030924}, "
            "u'recall': {u'1': "
            "0.008403361344537815, u'0': 0.9990321800145173, u'3': 0.030837004405286344, u'2': 0.0, u'4': 0.010416666666666666}, u'precision': {"
            "u'1': "
            "0.02564102564102564, u'0': 0.8796335747763102, u'3': 0.21212121212121213, u'2': 0, u'4': 1.0}, u'falseNegatives': {u'1': 118, u'0': 4, "
            "u'3': 220, "
            "u'2': 97, u'4': 190}, u'falsePositives': {u'1': 38, u'0': 565, u'3': 26}}, u'falseNegatives': 629, u'beta': 1.0, u'numLabels': 5, "
            "u'falsePositives': 4139}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 536769, u'subtype': u'evaluation', u'epoch': 56, u'values': {u'truePositives': 4397, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9221895973154363, u'precision': 0.9221895973154363, u'f': 0.9221895973154361}, u'macro': {u'recall': "
            "0.505175400940036, "
            "u'precision': 0.4611403044301217, u'f': 0.4821545109646343}, u'perLabel': {u'truePositives': {u'0': 4074, u'3': 177, u'4': 146}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9762760603882099, u'3': 0.5737439222042139, u'2': 0, u'4': 0.8179271708683473}, u'recall': {u'1': 0.0, "
            "u'0': 0.9857246552141302, "
            "u'3': 0.7797356828193832, u'2': 0.0, u'4': 0.7604166666666666}, u'precision': {u'1': 0, u'0': 0.9670068834559696, "
            "u'3': 0.45384615384615384, "
            "u'2': 0, u'4': 0.8848484848484849}, u'falseNegatives': {u'1': 119, u'0': 59, u'3': 50, u'2': 97, u'4': 46}, u'falsePositives': {u'0': "
            "139, "
            "u'3': 213, u'4': 19}}, u'falseNegatives': 371, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4397}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 160089, u'subtype': u'evaluation', u'epoch': 16, u'values': {u'truePositives': 34, "
            "u'numExamples': "
            "399, u'micro': {u'recall': 0.18681318681318682, u'precision': 0.13545816733067728, u'f': 0.15704387990762123}, u'macro': {u'recall': "
            "0.0787037037037037, u'precision': 0.034274193548387094, u'f': 0.04775280898876404}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 34, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0, u'3': 0.19101123595505615, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.3148148148148148, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0.13709677419354838, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 4, u'3': 74, u'2': 4, u'4': 66}, "
            "u'falsePositives': {u'3': 214, u'4': 3}}, u'falseNegatives': 148, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 34}, "
            "u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 150672, u'subtype': u'train', u'epoch': 15, u'values': {u'accumAccuracy': 67019.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.889613061657928}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 866364, u'subtype': u'evaluation', u'epoch': 91, u'values': {u'truePositives': 132, "
            "u'numExamples': "
            "429, u'micro': {u'recall': 0.5238095238095238, u'precision': 0.42718446601941745, u'f': 0.4705882352941177}, u'macro': {u'recall': "
            "0.38615888615888616, u'precision': 0.3538029538029538, u'f': 0.36927351434046446}, u'perLabel': {u'truePositives': {u'1': 19, "
            "u'3': 72, u'2': 0, "
            "u'4': 41}, u'f': {u'1': 0.34234234234234234, u'3': 0.47524752475247534, u'2': 0, u'4': 0.5734265734265734}, u'recall': {u'1': "
            "0.25675675675675674, "
            "u'3': 0.6666666666666666, u'2': 0.0, u'4': 0.6212121212121212}, u'precision': {u'1': 0.5135135135135135, u'3': 0.36923076923076925, "
            "u'2': 0, "
            "u'4': 0.5324675324675324}, u'falseNegatives': {u'1': 55, u'3': 36, u'2': 4, u'4': 25}, u'falsePositives': {u'1': 18, u'3': 123, "
            "u'4': 36}}, "
            "u'falseNegatives': 120, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 132}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 696858, u'subtype': u'evaluation', u'epoch': 73, u'values': {u'accumAccuracy': 4414.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.925755033557047}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 53, u'type': u'duration', u'iteration': 508518}",
            "{u'name': u'CustomMetricDev', u'iteration': 734526, u'subtype': u'evaluation', u'epoch': 77, u'values': {u'truePositives': 113, "
            "u'numExamples': "
            "446, u'micro': {u'recall': 0.44841269841269843, u'precision': 0.36807817589576547, u'f': 0.40429338103756707}, u'macro': {u'recall': "
            "0.32352238602238603, u'precision': 0.30780228758169936, u'f': 0.31546662015629995}, u'perLabel': {u'truePositives': {u'1': 7, "
            "u'3': 69, u'2': 0, "
            "u'4': 37}, u'f': {u'1': 0.15384615384615383, u'3': 0.4259259259259259, u'2': 0, u'4': 0.5285714285714286}, u'recall': {u'1': "
            "0.0945945945945946, "
            "u'3': 0.6388888888888888, u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 0.4117647058823529, u'3': 0.3194444444444444, "
            "u'2': 0, "
            "u'4': 0.5}, u'falseNegatives': {u'1': 67, u'3': 39, u'2': 4, u'4': 29}, u'falsePositives': {u'1': 10, u'3': 147, u'4': 37}}, "
            "u'falseNegatives': "
            "139, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 113}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 715692, u'subtype': u'train', u'epoch': 75, u'values': {u'loss': 0.16574684937325534, "
            "u'accumLoss': "
            "12486.538897534192, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 470850, u'subtype': u'evaluation', u'epoch': 49, u'values': {u'loss': 0.23728279769420624, "
            "u'accumLoss': "
            "1131.3643794059753, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 640356, u'subtype': u'evaluation', u'epoch': 67, u'values': {u'truePositives': 106, "
            "u'numExamples': "
            "456, u'micro': {u'recall': 0.42063492063492064, u'precision': 0.3419354838709677, u'f': 0.3772241992882563}, u'macro': {u'recall': "
            "0.3015913640913641, u'precision': 0.3826760832500441, u'f': 0.3373295117309232}, u'perLabel': {u'truePositives': {u'1': 3, u'3': 67, "
            "u'2': 0, "
            "u'4': 36}, u'f': {u'1': 0.07692307692307693, u'3': 0.39296187683284456, u'2': 0, u'4': 0.5179856115107914}, u'recall': {u'1': "
            "0.04054054054054054, "
            "u'3': 0.6203703703703703, u'2': 0.0, u'4': 0.5454545454545454}, u'precision': {u'1': 0.75, u'3': 0.2875536480686695, u'2': 0, "
            "u'4': 0.4931506849315068}, u'falseNegatives': {u'1': 71, u'3': 41, u'2': 4, u'4': 30}, u'falsePositives': {u'1': 1, u'3': 166, "
            "u'4': 37}}, "
            "u'falseNegatives': 146, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 106}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 904032, u'subtype': u'train', u'epoch': 95, u'values': {u'accumAccuracy': 71222.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9454038627463994}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 169506, u'subtype': u'evaluation', u'epoch': 17, u'values': {u'accumAccuracy': 4211.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8831795302013423}, u'type': u'metric'}",
            "{u'duration': 14, u'subtype': u'training', u'epoch': 8, u'type': u'duration', u'iteration': 84753}",
            "{u'name': u'LossTrain', u'iteration': 499101, u'subtype': u'train', u'epoch': 52, u'values': {u'loss': 0.19931012656234295, "
            "u'accumLoss': "
            "15015.028384574107, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 94170, u'subtype': u'train', u'epoch': 9, u'values': {u'accumAccuracy': 66258.0, u'numExamples': "
            "75335, "
            "u'accuracy': 0.8795115152319639}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 885198, u'subtype': u'train', u'epoch': 93, u'values': {u'loss': 0.1501082308811406, "
            "u'accumLoss': "
            "11308.403573430725, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 44, u'type': u'duration', u'iteration': 423765}",
            "{u'name': u'AccTrain', u'iteration': 235425, u'subtype': u'train', u'epoch': 24, u'values': {u'accumAccuracy': 67988.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9024756089467048}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 762777, u'subtype': u'evaluation', u'epoch': 80, u'values': {u'truePositives': 119, "
            "u'numExamples': "
            "450, u'micro': {u'recall': 0.4722222222222222, u'precision': 0.3753943217665615, u'f': 0.4182776801405975}, u'macro': {u'recall': "
            "0.3418304668304668, u'precision': 0.3095186583798809, u'f': 0.32487310841959394}, u'perLabel': {u'truePositives': {u'1': 7, u'3': 72, "
            "u'2': 0, "
            "u'4': 40}, u'f': {u'1': 0.15217391304347827, u'3': 0.4350453172205438, u'2': 0, u'4': 0.5633802816901409}, u'recall': {u'1': "
            "0.0945945945945946, "
            "u'3': 0.6666666666666666, u'2': 0.0, u'4': 0.6060606060606061}, u'precision': {u'1': 0.3888888888888889, u'3': 0.32286995515695066, "
            "u'2': 0, "
            "u'4': 0.5263157894736842}, u'falseNegatives': {u'1': 67, u'3': 36, u'2': 4, u'4': 26}, u'falsePositives': {u'1': 11, u'3': 151, "
            "u'4': 36}}, "
            "u'falseNegatives': 133, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 119}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 84753, u'subtype': u'evaluation', u'epoch': 8, u'values': {u'loss': 0.3676595985889435, "
            "u'accumLoss': "
            "1753.0009660720825, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 18, u'iteration': 169506}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 81, u'type': u'duration', u'iteration': 772194}",
            "{u'name': u'AccDev', u'iteration': 37668, u'subtype': u'evaluation', u'epoch': 3, u'values': {u'accumAccuracy': 4133.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8668204697986577}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 131838, u'subtype': u'train', u'epoch': 13, u'values': {u'accumAccuracy': 66802.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.8867325944116281}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 583854, u'subtype': u'evaluation', u'epoch': 61, u'values': {u'truePositives': 4400, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9228187919463087, u'precision': 0.9228187919463087, u'f': 0.9228187919463087}, u'macro': {u'recall': "
            "0.5058024021316909, "
            "u'precision': 0.4644241370169914, u'f': 0.4842309185177494}, u'perLabel': {u'truePositives': {u'0': 4077, u'3': 174, u'4': 149}, "
            "u'f': {u'1': 0, "
            "u'0': 0.975825753949258, u'3': 0.5742574257425742, u'2': 0, u'4': 0.8324022346368715}, u'recall': {u'1': 0.0, u'0': 0.9864505202032422, "
            "u'3': 0.7665198237885462, u'2': 0.0, u'4': 0.7760416666666666}, u'precision': {u'1': 0, u'0': 0.9654274212645039, "
            "u'3': 0.45910290237467016, "
            "u'2': 0, u'4': 0.8975903614457831}, u'falseNegatives': {u'1': 119, u'0': 56, u'3': 53, u'2': 97, u'4': 43}, u'falsePositives': {u'0': "
            "146, "
            "u'3': 205, u'4': 17}}, u'falseNegatives': 368, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4400}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 26, u'type': u'duration', u'iteration': 254259}",
            "{u'name': u'LossDev', u'iteration': 131838, u'subtype': u'evaluation', u'epoch': 13, u'values': {u'loss': 0.3331941068172455, "
            "u'accumLoss': "
            "1588.6695013046265, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 65919, u'subtype': u'evaluation', u'epoch': 6, u'values': {u'loss': 0.3950927257537842, "
            "u'accumLoss': "
            "1883.802116394043, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 86, u'type': u'duration', u'iteration': 819279}",
            "{u'name': u'AccTrain', u'iteration': 122421, u'subtype': u'train', u'epoch': 12, u'values': {u'accumAccuracy': 66677.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.8850733390854184}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 54, u'type': u'duration', u'iteration': 517935}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 48, u'type': u'duration', u'iteration': 461433}",
            "{u'name': u'AccTrain', u'iteration': 75336, u'subtype': u'train', u'epoch': 7, u'values': {u'accumAccuracy': 65785.0, u'numExamples': "
            "75335, "
            "u'accuracy': 0.8732328930775868}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 423765, u'subtype': u'evaluation', u'epoch': 44, u'values': {u'truePositives': 88, "
            "u'numExamples': "
            "441, u'micro': {u'recall': 0.4835164835164835, u'precision': 0.25360230547550433, u'f': 0.33270321361058597}, u'macro': {u'recall': "
            "0.24494949494949497, u'precision': 0.14367977528089887, u'f': 0.18112011155849705}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 60, u'2': 0, "
            "u'4': 28}, u'f': {u'1': 0, u'3': 0.32, u'2': 0, u'4': 0.3835616438356164}, u'recall': {u'1': 0.0, u'3': 0.5555555555555556, u'2': 0.0, "
            "u'4': 0.42424242424242425}, u'precision': {u'1': 0, u'3': 0.2247191011235955, u'2': 0, u'4': 0.35}, u'falseNegatives': {u'1': 4, "
            "u'3': 48, "
            "u'2': 4, u'4': 38}, u'falsePositives': {u'3': 207, u'4': 52}}, u'falseNegatives': 94, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 88}, "
            "u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 47, u'iteration': 442599}",
            "{u'name': u'CustomMetricDev', u'iteration': 150672, u'subtype': u'evaluation', u'epoch': 15, u'values': {u'truePositives': 29, "
            "u'numExamples': "
            "390, u'micro': {u'recall': 0.15934065934065933, u'precision': 0.12236286919831224, u'f': 0.13842482100238662}, u'macro': {u'recall': "
            "0.06712962962962964, u'precision': 0.03072033898305085, u'f': 0.04215116279069768}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 29, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0, u'3': 0.16860465116279072, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.26851851851851855, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0.1228813559322034, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 4, u'3': 79, u'2': 4, u'4': 66}, "
            "u'falsePositives': {u'3': 207, u'4': 1}}, u'falseNegatives': 153, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 29}, "
            "u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 320178, u'subtype': u'train', u'epoch': 33, u'values': {u'loss': 0.24627002444776994, "
            "u'accumLoss': "
            "18552.752291772747, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 178923, u'subtype': u'train', u'epoch': 18, u'values': {u'accumAccuracy': 67366.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.8942191544434858}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 63, u'type': u'duration', u'iteration': 602688}",
            "{u'name': u'LossDev', u'iteration': 499101, u'subtype': u'evaluation', u'epoch': 52, u'values': {u'loss': 0.23200646042823792, "
            "u'accumLoss': "
            "1106.2068033218384, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 696858, u'subtype': u'train', u'epoch': 73, u'values': {u'accumAccuracy': 70633.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9375854516492997}, u'type': u'metric'}",
            "{u'duration': 14, u'subtype': u'training', u'epoch': 7, u'type': u'duration', u'iteration': 75336}",
            "{u'name': u'FMetricDev', u'iteration': 922866, u'subtype': u'evaluation', u'epoch': 97, u'values': {u'truePositives': 4450, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9333053691275168, u'precision': 0.9333053691275168, u'f': 0.9333053691275168}, u'macro': {u'recall': "
            "0.5941031087873301, "
            "u'precision': 0.7046785125621529, u'f': 0.6446837376306754}, u'perLabel': {u'truePositives': {u'1': 36, u'0': 4065, u'3': 185, u'2': 3, "
            "u'4': 161}, u'f': {u'1': 0.4137931034482758, u'0': 0.9777510523150932, u'3': 0.6595365418894831, u'2': 0.05825242718446602, "
            "u'4': 0.8407310704960834}, u'recall': {u'1': 0.3025210084033613, u'0': 0.9835470602467941, u'3': 0.8149779735682819, "
            "u'2': 0.030927835051546393, "
            "u'4': 0.8385416666666666}, u'precision': {u'1': 0.6545454545454545, u'0': 0.9720229555236729, u'3': 0.5538922155688623, u'2': 0.5, "
            "u'4': 0.8429319371727748}, u'falseNegatives': {u'1': 83, u'0': 68, u'3': 42, u'2': 94, u'4': 31}, u'falsePositives': {u'1': 19, "
            "u'0': 117, "
            "u'3': 149, u'2': 3, u'4': 30}}, u'falseNegatives': 318, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4450}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 65919, u'subtype': u'evaluation', u'epoch': 6, u'values': {u'truePositives': 4154, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8712248322147651, u'precision': 0.8712248322147651, u'f': 0.8712248322147651}, u'macro': {u'recall': "
            "0.2311550231135408, "
            "u'precision': 0.4443365789157351, u'f': 0.3041063186008548}, u'perLabel': {u'truePositives': {u'1': 3, u'0': 4123, u'3': 16, u'4': 12}, "
            "u'f': {u'1': 0.03614457831325301, u'0': 0.9388591597404077, u'3': 0.1118881118881119, u'2': 0, u'4': 0.11764705882352941}, "
            "u'recall': {u'1': "
            "0.025210084033613446, u'0': 0.9975804500362933, u'3': 0.07048458149779736, u'2': 0.0, u'4': 0.0625}, u'precision': {u'1': "
            "0.06382978723404255, "
            "u'0': 0.8866666666666667, u'3': 0.2711864406779661, u'2': 0, u'4': 1.0}, u'falseNegatives': {u'1': 116, u'0': 10, u'3': 211, u'2': 97, "
            "u'4': 180}, "
            "u'falsePositives': {u'1': 44, u'0': 527, u'3': 43}}, u'falseNegatives': 614, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4154}, "
            "u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 113004, u'subtype': u'evaluation', u'epoch': 11, u'values': {u'truePositives': 4186, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8779362416107382, u'precision': 0.8779362416107382, u'f': 0.8779362416107382}, u'macro': {u'recall': "
            "0.2724425870566626, "
            "u'precision': 0.2602488743369627, u'f': 0.2662061690174292}, u'perLabel': {u'truePositives': {u'1': 2, u'0': 4104, u'3': 80}, "
            "u'f': {u'1': "
            "0.028169014084507043, u'0': 0.9534208386572193, u'3': 0.3225806451612903, u'2': 0, u'4': 0}, u'recall': {u'1': 0.01680672268907563, "
            "u'0': 0.9929833051052505, u'3': 0.3524229074889868, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0.08695652173913043, "
            "u'0': 0.9168900804289544, "
            "u'3': 0.29739776951672864, u'2': 0, u'4': 0}, u'falseNegatives': {u'1': 117, u'0': 29, u'3': 147, u'2': 97, u'4': 192}, "
            "u'falsePositives': {u'1': "
            "21, u'0': 372, u'3': 189}}, u'falseNegatives': 582, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4186}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 527352, u'subtype': u'evaluation', u'epoch': 55, u'values': {u'truePositives': 4393, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9213506711409396, u'precision': 0.9213506711409396, u'f': 0.9213506711409396}, u'macro': {u'recall': "
            "0.5004972867998094, "
            "u'precision': 0.4603943245719983, u'f': 0.4796089539742164}, u'perLabel': {u'truePositives': {u'0': 4075, u'3': 174, u'4': 144}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9755805602106775, u'3': 0.569558101472995, u'2': 0, u'4': 0.8112676056338027}, u'recall': {u'1': 0.0, u'0': 0.9859666102105008, "
            "u'3': 0.7665198237885462, u'2': 0.0, u'4': 0.75}, u'precision': {u'1': 0, u'0': 0.9654110400379057, u'3': 0.453125, u'2': 0, "
            "u'4': 0.8834355828220859}, u'falseNegatives': {u'1': 119, u'0': 58, u'3': 53, u'2': 97, u'4': 48}, u'falsePositives': {u'0': 146, "
            "u'3': 210, "
            "u'4': 19}}, u'falseNegatives': 375, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4393}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 2, u'iteration': 18834}",
            "{u'name': u'FMetricDev', u'iteration': 875781, u'subtype': u'evaluation', u'epoch': 92, u'values': {u'truePositives': 4446, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9324664429530202, u'precision': 0.9324664429530202, u'f': 0.9324664429530202}, u'macro': {u'recall': "
            "0.5764101306210494, "
            "u'precision': 0.611062778852941, u'f': 0.593230840663654}, u'perLabel': {u'truePositives': {u'1': 30, u'0': 4072, u'3': 183, "
            "u'4': 161}, "
            "u'f': {u'1': 0.37037037037037035, u'0': 0.9777884499939967, u'3': 0.646643109540636, u'2': 0, u'4': 0.8429319371727747}, "
            "u'recall': {u'1': "
            "0.25210084033613445, u'0': 0.9852407452213888, u'3': 0.8061674008810573, u'2': 0.0, u'4': 0.8385416666666666}, u'precision': {u'1': "
            "0.6976744186046512, u'0': 0.9704480457578646, u'3': 0.5398230088495575, u'2': 0, u'4': 0.8473684210526315}, u'falseNegatives': {u'1': "
            "89, "
            "u'0': 61, u'3': 44, u'2': 97, u'4': 31}, u'falsePositives': {u'1': 13, u'0': 124, u'3': 156, u'4': 29}}, u'falseNegatives': 322, "
            "u'beta': 1.0, "
            "u'numLabels': 5, u'falsePositives': 4446}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 734526, u'subtype': u'evaluation', u'epoch': 77, u'values': {u'accumAccuracy': 4423.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9276426174496645}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 65919, u'subtype': u'train', u'epoch': 6, u'values': {u'accumAccuracy': 65529.0, u'numExamples': "
            "75335, "
            "u'accuracy': 0.8698347381695095}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 30, u'type': u'duration', u'iteration': 291927}",
            "{u'learn_rate': [0.001], u'epoch': 91, u'iteration': 856947}",
            "{u'name': u'LossDev', u'iteration': 386097, u'subtype': u'evaluation', u'epoch': 40, u'values': {u'loss': 0.25633010268211365, "
            "u'accumLoss': "
            "1222.1819295883179, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 95, u'type': u'duration', u'iteration': 904032}",
            "{u'learn_rate': [0.001], u'epoch': 51, u'iteration': 480267}",
            "{u'name': u'AccDev', u'iteration': 593271, u'subtype': u'evaluation', u'epoch': 62, u'values': {u'accumAccuracy': 4401.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9230285234899329}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 65, u'type': u'duration', u'iteration': 621522}",
            "{u'learn_rate': [0.001], u'epoch': 43, u'iteration': 404931}", "{u'learn_rate': [0.001], u'epoch': 22, u'iteration': 207174}",
            "{u'name': u'CustomMetricDev', u'iteration': 517935, u'subtype': u'evaluation', u'epoch': 54, u'values': {u'truePositives': 102, "
            "u'numExamples': "
            "427, u'micro': {u'recall': 0.5604395604395604, u'precision': 0.29394812680115273, u'f': 0.385633270321361}, u'macro': {u'recall': "
            "0.28766835016835013, u'precision': 0.16991486424298205, u'f': 0.2136403920704978}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 67, "
            "u'2': 0, "
            "u'4': 35}, u'f': {u'1': 0, u'3': 0.3592493297587131, u'2': 0, u'4': 0.47297297297297297}, u'recall': {u'1': 0.0, "
            "u'3': 0.6203703703703703, "
            "u'2': 0.0, u'4': 0.5303030303030303}, u'precision': {u'1': 0, u'3': 0.2528301886792453, u'2': 0, u'4': 0.4268292682926829}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 41, u'2': 4, u'4': 31}, u'falsePositives': {u'3': 198, u'4': 47}}, u'falseNegatives': 80, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 102}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 216591, u'subtype': u'train', u'epoch': 22, u'values': {u'loss': 0.2792135705145375, "
            "u'accumLoss': "
            "21034.55433471268, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 88, u'iteration': 828696}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 79, u'type': u'duration', u'iteration': 753360}",
            "{u'name': u'CustomMetricDev', u'iteration': 809862, u'subtype': u'evaluation', u'epoch': 85, u'values': {u'truePositives': 126, "
            "u'numExamples': "
            "501, u'micro': {u'recall': 0.4131147540983607, u'precision': 0.391304347826087, u'f': 0.40191387559808617}, u'macro': {u'recall': "
            "0.3658886158886159, u'precision': 0.3275913714602081, u'f': 0.3456825162002485}, u'perLabel': {u'truePositives': {u'1': 13, u'3': 72, "
            "u'2': 0, "
            "u'4': 41}, u'f': {u'1': 0.25242718446601947, u'3': 0.4472049689440994, u'2': 0, u'4': 0.5694444444444445}, u'recall': {u'1': "
            "0.17567567567567569, "
            "u'3': 0.6666666666666666, u'2': 0.0, u'4': 0.6212121212121212}, u'precision': {u'1': 0.4482758620689655, u'3': 0.3364485981308411, "
            "u'2': 0.0, "
            "u'4': 0.5256410256410257}, u'falseNegatives': {u'1': 61, u'3': 36, u'2': 57, u'4': 25}, u'falsePositives': {u'1': 16, u'3': 142, "
            "u'2': 1, "
            "u'4': 37}}, u'falseNegatives': 179, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 126}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 433182, u'subtype': u'train', u'epoch': 45, u'values': {u'accumAccuracy': 69690.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9250680294683746}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 207174, u'subtype': u'train', u'epoch': 21, u'values': {u'accumAccuracy': 67699.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.8986394106325082}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 254259, u'subtype': u'train', u'epoch': 26, u'values': {u'loss': 0.2665670465966639, "
            "u'accumLoss': "
            "20081.828455359675, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 78, u'iteration': 734526}", "{u'learn_rate': [0.001], u'epoch': 42, u'iteration': 395514}",
            "{u'duration': 14, u'subtype': u'training', u'epoch': 3, u'type': u'duration', u'iteration': 37668}",
            "{u'name': u'LossTrain', u'iteration': 762777, u'subtype': u'train', u'epoch': 80, u'values': {u'loss': 0.16078663429618095, "
            "u'accumLoss': "
            "12112.861094702792, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 668607, u'subtype': u'evaluation', u'epoch': 70, u'values': {u'accumAccuracy': 4411.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9251258389261745}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 96, u'iteration': 904032}",
            "{u'name': u'FMetricDev', u'iteration': 291927, u'subtype': u'evaluation', u'epoch': 30, u'values': {u'truePositives': 4322, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9064597315436241, u'precision': 0.9064597315436241, u'f': 0.9064597315436241}, u'macro': {u'recall': "
            "0.4186348804063707, "
            "u'precision': 0.4434254140277873, u'f': 0.4306736927085008}, u'perLabel': {u'truePositives': {u'0': 4087, u'3': 149, u'4': 86}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9690574985180793, u'3': 0.5025295109612141, u'2': 0, u'4': 0.589041095890411}, u'recall': {u'1': 0.0, u'0': 0.988870070166949, "
            "u'3': 0.6563876651982379, u'2': 0.0, u'4': 0.4479166666666667}, u'precision': {u'1': 0, u'0': 0.9500232450023245, "
            "u'3': 0.40710382513661203, "
            "u'2': 0, u'4': 0.86}, u'falseNegatives': {u'1': 119, u'0': 46, u'3': 78, u'2': 97, u'4': 106}, u'falsePositives': {u'0': 215, "
            "u'3': 217, "
            "u'4': 14}}, u'falseNegatives': 446, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4322}, u'type': u'metric'}",
            u'Training...', u'Number of batches: 9417', "{u'learn_rate': [0.001], u'epoch': 65, u'iteration': 612105}",
            "{u'name': u'CustomMetricDev', u'iteration': 207174, u'subtype': u'evaluation', u'epoch': 21, u'values': {u'truePositives': 41, "
            "u'numExamples': "
            "427, u'micro': {u'recall': 0.22527472527472528, u'precision': 0.14335664335664336, u'f': 0.17521367521367523}, u'macro': {u'recall': "
            "0.09490740740740741, u'precision': 0.03810408921933085, u'f': 0.054376657824933686}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 41, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0, u'3': 0.21750663129973474, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.37962962962962965, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0.1524163568773234, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 4, u'3': 67, u'2': 4, u'4': 66}, "
            "u'falsePositives': {u'3': 228, u'4': 17}}, u'falseNegatives': 141, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 41}, "
            "u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 687441, u'subtype': u'evaluation', u'epoch': 72, u'values': {u'truePositives': 4414, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.925755033557047, u'precision': 0.925755033557047, u'f': 0.925755033557047}, u'macro': {u'recall': "
            "0.5260422790257746, "
            "u'precision': 0.6420318444502536, u'f': 0.578278189498244}, u'perLabel': {u'truePositives': {u'1': 7, u'0': 4075, u'3': 179, "
            "u'4': 153}, "
            "u'f': {u'1': 0.11023622047244094, u'0': 0.9763987061219599, u'3': 0.5956738768718802, u'2': 0, u'4': 0.8406593406593407}, "
            "u'recall': {u'1': "
            "0.058823529411764705, u'0': 0.9859666102105008, u'3': 0.788546255506608, u'2': 0.0, u'4': 0.796875}, u'precision': {u'1': 0.875, "
            "u'0': 0.9670147128618889, u'3': 0.4786096256684492, u'2': 0, u'4': 0.8895348837209303}, u'falseNegatives': {u'1': 112, u'0': 58, "
            "u'3': 48, "
            "u'2': 97, u'4': 39}, u'falsePositives': {u'1': 1, u'0': 139, u'3': 195, u'4': 19}}, u'falseNegatives': 354, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4414}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 84753, u'subtype': u'train', u'epoch': 8, u'values': {u'accumAccuracy': 66007.0, u'numExamples': "
            "75335, "
            "u'accuracy': 0.876179730536935}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 452016, u'subtype': u'evaluation', u'epoch': 47, u'values': {u'truePositives': 4374, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9173657718120806, u'precision': 0.9173657718120806, u'f': 0.9173657718120806}, u'macro': {u'recall': "
            "0.47686350758178947, "
            "u'precision': 0.4503349488624269, u'f': 0.46321971700590886}, u'perLabel': {u'truePositives': {u'0': 4080, u'3': 167, u'4': 127}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9744447098160973, u'3': 0.5529801324503312, u'2': 0, u'4': 0.7426900584795322}, u'recall': {u'1': 0.0, "
            "u'0': 0.9871763851923542, "
            "u'3': 0.73568281938326, u'2': 0.0, u'4': 0.6614583333333334}, u'precision': {u'1': 0, u'0': 0.9620372553643008, "
            "u'3': 0.44297082228116713, "
            "u'2': 0, u'4': 0.8466666666666667}, u'falseNegatives': {u'1': 119, u'0': 53, u'3': 60, u'2': 97, u'4': 65}, u'falsePositives': {u'0': "
            "161, "
            "u'3': 210, u'4': 23}}, u'falseNegatives': 394, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4374}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 50, u'type': u'duration', u'iteration': 480267}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 76, u'type': u'duration', u'iteration': 725109}",
            "{u'name': u'FMetricDev', u'iteration': 282510, u'subtype': u'evaluation', u'epoch': 29, u'values': {u'truePositives': 4308, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9035234899328859, u'precision': 0.9035234899328859, u'f': 0.9035234899328859}, u'macro': {u'recall': "
            "0.4078640403446633, "
            "u'precision': 0.434335904645183, u'f': 0.42068394325880537}, u'perLabel': {u'truePositives': {u'0': 4083, u'3': 150, u'4': 75}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9694883058292769, u'3': 0.4878048780487805, u'2': 0, u'4': 0.5319148936170213}, u'recall': {u'1': 0.0, "
            "u'0': 0.9879022501814663, "
            "u'3': 0.6607929515418502, u'2': 0.0, u'4': 0.390625}, u'precision': {u'1': 0, u'0': 0.9517482517482517, u'3': 0.3865979381443299, "
            "u'2': 0, "
            "u'4': 0.8333333333333334}, u'falseNegatives': {u'1': 119, u'0': 50, u'3': 77, u'2': 97, u'4': 117}, u'falsePositives': {u'0': 207, "
            "u'3': 238, "
            "u'4': 15}}, u'falseNegatives': 460, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4308}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 14, u'iteration': 131838}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 88, u'type': u'duration', u'iteration': 838113}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 34, u'type': u'duration', u'iteration': 329595}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 29, u'type': u'duration', u'iteration': 282510}",
            "{u'name': u'FMetricDev', u'iteration': 28251, u'subtype': u'evaluation', u'epoch': 2, u'values': {u'truePositives': 4133, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8668204697986577, u'precision': 0.8668204697986577, u'f': 0.8668204697986577}, u'macro': {u'recall': 0.2, "
            "u'precision': "
            "0.17336409395973154, u'f': 0.18573194023143466}, u'perLabel': {u'truePositives': {u'0': 4133}, u'f': {u'1': 0, "
            "u'0': 0.9286597011571733, u'3': 0, "
            "u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'0': 1.0, u'3': 0.0, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0, "
            "u'0': 0.8668204697986577, u'3': 0, "
            "u'2': 0, u'4': 0}, u'falseNegatives': {u'1': 119, u'3': 227, u'2': 97, u'4': 192}, u'falsePositives': {u'0': 635}}, u'falseNegatives': "
            "635, "
            "u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4133}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 235425, u'subtype': u'train', u'epoch': 24, u'values': {u'loss': 0.2727346669512096, "
            "u'accumLoss': "
            "20546.466134769376, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 687441, u'subtype': u'evaluation', u'epoch': 72, u'values': {u'accumAccuracy': 4414.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.925755033557047}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 45, u'type': u'duration', u'iteration': 433182}",
            "{u'learn_rate': [0.001], u'epoch': 27, u'iteration': 254259}",
            "{u'name': u'CustomMetricDev', u'iteration': 65919, u'subtype': u'evaluation', u'epoch': 6, u'values': {u'truePositives': 4, "
            "u'numExamples': 361, "
            "u'micro': {u'recall': 0.015873015873015872, u'precision': 0.035398230088495575, u'f': 0.021917808219178082}, u'macro': {u'recall': "
            "0.011386386386386387, u'precision': 0.020039682539682538, u'f': 0.014521674282211227}, u'perLabel': {u'truePositives': {u'1': 2, "
            "u'3': 2, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0.03361344537815126, u'3': 0.024390243902439025, u'2': 0, u'4': 0}, u'recall': {u'1': 0.02702702702702703, "
            "u'3': 0.018518518518518517, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0.044444444444444446, u'3': 0.03571428571428571, u'2': 0, "
            "u'4': 0.0}, "
            "u'falseNegatives': {u'1': 72, u'3': 106, u'2': 4, u'4': 66}, u'falsePositives': {u'1': 43, u'3': 54, u'4': 12}}, u'falseNegatives': "
            "248, "
            "u'beta': 1.0, u'numLabels': 4, u'falsePositives': 4}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 339012, u'subtype': u'evaluation', u'epoch': 35, u'values': {u'loss': 0.26941201090812683, "
            "u'accumLoss': "
            "1284.5564680099487, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 772194, u'subtype': u'train', u'epoch': 81, u'values': {u'loss': 0.15980322817670106, "
            "u'accumLoss': "
            "12038.776194691774, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 6, u'type': u'duration', u'iteration': 65919}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 98, u'type': u'duration', u'iteration': 932283}",
            "{u'name': u'AccTrain', u'iteration': 18834, u'subtype': u'train', u'epoch': 1, u'values': {u'accumAccuracy': 65313.0, u'numExamples': "
            "75335, "
            "u'accuracy': 0.8669675449658193}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 847530, u'subtype': u'evaluation', u'epoch': 89, u'values': {u'loss': 0.194245845079422, "
            "u'accumLoss': "
            "926.1641893386841, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 791028, u'subtype': u'evaluation', u'epoch': 83, u'values': {u'loss': 0.1979272961616516, "
            "u'accumLoss': "
            "943.7173480987549, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 67, u'iteration': 630939}",
            "{u'name': u'LossTrain', u'iteration': 932283, u'subtype': u'train', u'epoch': 98, u'values': {u'loss': 0.14647758194168164, "
            "u'accumLoss': "
            "11034.888635576586, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 97, u'type': u'duration', u'iteration': 922866}",
            "{u'name': u'CustomMetricDev', u'iteration': 630939, u'subtype': u'evaluation', u'epoch': 66, u'values': {u'truePositives': 108, "
            "u'numExamples': "
            "469, u'micro': {u'recall': 0.42857142857142855, u'precision': 0.3323076923076923, u'f': 0.37435008665511266}, u'macro': {u'recall': "
            "0.30769405769405767, u'precision': 0.3785982814178303, u'f': 0.3394834381983591}, u'perLabel': {u'truePositives': {u'1': 3, u'3': 68, "
            "u'2': 0, "
            "u'4': 37}, u'f': {u'1': 0.07692307692307693, u'3': 0.38526912181303113, u'2': 0, u'4': 0.5211267605633803}, u'recall': {u'1': "
            "0.04054054054054054, "
            "u'3': 0.6296296296296297, u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 0.75, u'3': 0.27755102040816326, u'2': 0, "
            "u'4': 0.4868421052631579}, u'falseNegatives': {u'1': 71, u'3': 40, u'2': 4, u'4': 29}, u'falsePositives': {u'1': 1, u'3': 177, "
            "u'4': 39}}, "
            "u'falseNegatives': 144, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 108}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 630939, u'subtype': u'train', u'epoch': 66, u'values': {u'accumAccuracy': 70420.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9347580805734387}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 188340, u'subtype': u'evaluation', u'epoch': 19, u'values': {u'loss': 0.3107079267501831, "
            "u'accumLoss': "
            "1481.455394744873, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 913449, u'subtype': u'evaluation', u'epoch': 96, u'values': {u'truePositives': 4449, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9330956375838926, u'precision': 0.9330956375838926, u'f': 0.9330956375838926}, u'macro': {u'recall': "
            "0.5883955071767646, "
            "u'precision': 0.6737431601122866, u'f': 0.6281836674137111}, u'perLabel': {u'truePositives': {u'1': 35, u'0': 4067, u'3': 185, u'2': 1, "
            "u'4': 161}, u'f': {u'1': 0.4093567251461988, u'0': 0.9779968738727906, u'3': 0.654867256637168, u'2': 0.02, u'4': 0.8407310704960834}, "
            "u'recall': {u'1': 0.29411764705882354, u'0': 0.9840309702395355, u'3': 0.8149779735682819, u'2': 0.010309278350515464, "
            "u'4': 0.8385416666666666}, "
            "u'precision': {u'1': 0.6730769230769231, u'0': 0.972036328871893, u'3': 0.5473372781065089, u'2': 0.3333333333333333, "
            "u'4': 0.8429319371727748}, "
            "u'falseNegatives': {u'1': 84, u'0': 66, u'3': 42, u'2': 96, u'4': 31}, u'falsePositives': {u'1': 17, u'0': 117, u'3': 153, u'2': 2, "
            "u'4': 30}}, "
            "u'falseNegatives': 319, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4449}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 244842, u'subtype': u'evaluation', u'epoch': 25, u'values': {u'truePositives': 48, "
            "u'numExamples': "
            "475, u'micro': {u'recall': 0.26373626373626374, u'precision': 0.14076246334310852, u'f': 0.1835564053537285}, u'macro': {u'recall': "
            "0.1111111111111111, u'precision': 0.041379310344827586, u'f': 0.06030150753768845}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 48, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0, u'3': 0.2412060301507538, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.4444444444444444, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0.16551724137931034, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 4, u'3': 60, u'2': 4, u'4': 66}, "
            "u'falsePositives': {u'3': 242, u'4': 51}}, u'falseNegatives': 134, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 48}, "
            "u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 828696, u'subtype': u'evaluation', u'epoch': 87, u'values': {u'accumAccuracy': 4436.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9303691275167785}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 310761, u'subtype': u'evaluation', u'epoch': 32, u'values': {u'accumAccuracy': 4336.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9093959731543624}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 226008, u'subtype': u'evaluation', u'epoch': 23, u'values': {u'truePositives': 4254, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8921979865771812, u'precision': 0.8921979865771812, u'f': 0.8921979865771812}, u'macro': {u'recall': "
            "0.3504305359995992, "
            "u'precision': 0.4232529811200131, u'f': 0.38341457651703825}, u'perLabel': {u'truePositives': {u'0': 4085, u'3': 145, u'4': 24}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9670928030303031, u'3': 0.44546850998463905, u'2': 0, u'4': 0.2171945701357466}, u'recall': {u'1': 0.0, "
            "u'0': 0.9883861601742076, "
            "u'3': 0.6387665198237885, u'2': 0.0, u'4': 0.125}, u'precision': {u'1': 0, u'0': 0.9466975666280417, u'3': 0.3419811320754717, u'2': 0, "
            "u'4': 0.8275862068965517}, u'falseNegatives': {u'1': 119, u'0': 48, u'3': 82, u'2': 97, u'4': 168}, u'falsePositives': {u'0': 230, "
            "u'3': 279, "
            "u'4': 5}}, u'falseNegatives': 514, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4254}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 593271, u'subtype': u'evaluation', u'epoch': 62, u'values': {u'truePositives': 4401, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9230285234899329, u'precision': 0.9230285234899329, u'f': 0.9230285234899329}, u'macro': {u'recall': "
            "0.5109743488763361, "
            "u'precision': 0.6636351777120726, u'f': 0.5773843054172352}, u'perLabel': {u'truePositives': {u'1': 1, u'0': 4073, u'3': 177, "
            "u'4': 150}, "
            "u'f': {u'1': 0.016666666666666666, u'0': 0.9760364246345555, u'3': 0.5774877650897227, u'2': 0, u'4': 0.8333333333333334}, "
            "u'recall': {u'1': "
            "0.008403361344537815, u'0': 0.9854827002177595, u'3': 0.7797356828193832, u'2': 0.0, u'4': 0.78125}, u'precision': {u'1': 1.0, "
            "u'0': 0.9667695229052932, u'3': 0.4585492227979275, u'2': 0, u'4': 0.8928571428571429}, u'falseNegatives': {u'1': 118, u'0': 60, "
            "u'3': 50, "
            "u'2': 97, u'4': 42}, u'falsePositives': {u'0': 140, u'3': 209, u'4': 18}}, u'falseNegatives': 367, u'beta': 1.0, u'numLabels': 5, "
            "u'falsePositives': 4401}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 414348, u'subtype': u'evaluation', u'epoch': 43, u'values': {u'truePositives': 84, "
            "u'numExamples': "
            "431, u'micro': {u'recall': 0.46153846153846156, u'precision': 0.25225225225225223, u'f': 0.32621359223300966}, u'macro': {u'recall': "
            "0.23569023569023567, u'precision': 0.14372570517292932, u'f': 0.17856258358512062}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 56, u'2': 0, "
            "u'4': 28}, u'f': {u'1': 0, u'3': 0.30939226519337015, u'2': 0, u'4': 0.3862068965517242}, u'recall': {u'1': 0.0, "
            "u'3': 0.5185185185185185, "
            "u'2': 0.0, u'4': 0.42424242424242425}, u'precision': {u'1': 0, u'3': 0.2204724409448819, u'2': 0, u'4': 0.35443037974683544}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 52, u'2': 4, u'4': 38}, u'falsePositives': {u'3': 198, u'4': 51}}, u'falseNegatives': 98, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 84}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 7, u'type': u'duration', u'iteration': 75336}",
            "{u'name': u'AccTrain', u'iteration': 141255, u'subtype': u'train', u'epoch': 14, u'values': {u'accumAccuracy': 66906.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.8881130948430345}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 301344, u'subtype': u'evaluation', u'epoch': 31, u'values': {u'truePositives': 64, "
            "u'numExamples': "
            "449, u'micro': {u'recall': 0.3516483516483517, u'precision': 0.1933534743202417, u'f': 0.24951267056530213}, u'macro': {u'recall': "
            "0.17024410774410775, u'precision': 0.10172500559159026, u'f': 0.12735330567356398}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 49, u'2': 0, "
            "u'4': 15}, u'f': {u'1': 0, u'3': 0.2641509433962264, u'2': 0, u'4': 0.22388059701492535}, u'recall': {u'1': 0.0, "
            "u'3': 0.4537037037037037, "
            "u'2': 0.0, u'4': 0.22727272727272727}, u'precision': {u'1': 0, u'3': 0.18631178707224336, u'2': 0, u'4': 0.22058823529411764}, "
            "u'falseNegatives': "
            "{u'1': 4, u'3': 59, u'2': 4, u'4': 51}, u'falsePositives': {u'3': 214, u'4': 53}}, u'falseNegatives': 118, u'beta': 1.0, "
            "u'numLabels': 4, "
            "u'falsePositives': 64}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 94170, u'subtype': u'evaluation', u'epoch': 9, u'values': {u'truePositives': 12, "
            "u'numExamples': 420, "
            "u'micro': {u'recall': 0.047619047619047616, u'precision': 0.06666666666666667, u'f': 0.05555555555555555}, u'macro': {u'recall': "
            "0.02884134134134134, u'precision': 0.028063799717343026, u'f': 0.028447258434812564}, u'perLabel': {u'truePositives': {u'1': 1, "
            "u'3': 11, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0.017699115044247787, u'3': 0.09361702127659575, u'2': 0, u'4': 0}, u'recall': {u'1': 0.013513513513513514, "
            "u'3': 0.10185185185185185, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0.02564102564102564, u'3': 0.08661417322834646, u'2': 0, "
            "u'4': 0.0}, "
            "u'falseNegatives': {u'1': 73, u'3': 97, u'2': 4, u'4': 66}, u'falsePositives': {u'1': 38, u'3': 116, u'4': 14}}, u'falseNegatives': "
            "240, "
            "u'beta': 1.0, u'numLabels': 4, u'falsePositives': 12}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 66, u'iteration': 621522}",
            "{u'name': u'AccDev', u'iteration': 791028, u'subtype': u'evaluation', u'epoch': 83, u'values': {u'accumAccuracy': 4432.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9295302013422819}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 809862, u'subtype': u'evaluation', u'epoch': 85, u'values': {u'accumAccuracy': 4430.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9291107382550335}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 291927, u'subtype': u'evaluation', u'epoch': 30, u'values': {u'loss': 0.28149253129959106, "
            "u'accumLoss': "
            "1342.1563892364502, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 13, u'iteration': 122421}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 84, u'type': u'duration', u'iteration': 800445}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 45, u'type': u'duration', u'iteration': 433182}",
            "{u'name': u'CustomMetricDev', u'iteration': 885198, u'subtype': u'evaluation', u'epoch': 93, u'values': {u'truePositives': 134, "
            "u'numExamples': "
            "483, u'micro': {u'recall': 0.43934426229508194, u'precision': 0.42948717948717946, u'f': 0.4343598055105348}, u'macro': {u'recall': "
            "0.39250614250614246, u'precision': 0.3484432234432234, u'f': 0.36916451191201005}, u'perLabel': {u'truePositives': {u'1': 22, "
            "u'3': 72, u'2': 0, "
            "u'4': 40}, u'f': {u'1': 0.3728813559322034, u'3': 0.4848484848484849, u'2': 0, u'4': 0.5555555555555556}, u'recall': {u'1': "
            "0.2972972972972973, "
            "u'3': 0.6666666666666666, u'2': 0.0, u'4': 0.6060606060606061}, u'precision': {u'1': 0.5, u'3': 0.38095238095238093, u'2': 0.0, "
            "u'4': 0.5128205128205128}, u'falseNegatives': {u'1': 52, u'3': 36, u'2': 57, u'4': 26}, u'falsePositives': {u'1': 22, u'3': 117, "
            "u'2': 1, "
            "u'4': 38}}, u'falseNegatives': 171, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 134}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 37668, u'subtype': u'evaluation', u'epoch': 3, u'values': {u'loss': 0.45998823642730713, "
            "u'accumLoss': "
            "2193.2239112854004, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 433182, u'subtype': u'evaluation', u'epoch': 45, u'values': {u'accumAccuracy': 4372.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9169463087248322}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 36, u'type': u'duration', u'iteration': 348429}",
            "{u'name': u'FMetricDev', u'iteration': 414348, u'subtype': u'evaluation', u'epoch': 43, u'values': {u'truePositives': 4361, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9146392617449665, u'precision': 0.9146392617449665, u'f': 0.9146392617449665}, u'macro': {u'recall': "
            "0.46111544162293894, "
            "u'precision': 0.4439805910676705, u'f': 0.4523858218968999}, u'perLabel': {u'truePositives': {u'0': 4084, u'3': 156, u'4': 121}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9724967258006906, u'3': 0.5360824742268041, u'2': 0, u'4': 0.7138643067846608}, u'recall': {u'1': 0.0, u'0': 0.988144205177837, "
            "u'3': 0.6872246696035242, u'2': 0.0, u'4': 0.6302083333333334}, u'precision': {u'1': 0, u'0': 0.9573370839193625, "
            "u'3': 0.4394366197183099, "
            "u'2': 0, u'4': 0.8231292517006803}, u'falseNegatives': {u'1': 119, u'0': 49, u'3': 71, u'2': 97, u'4': 71}, u'falsePositives': {u'0': "
            "182, "
            "u'3': 199, u'4': 26}}, u'falseNegatives': 407, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4361}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 433182, u'subtype': u'evaluation', u'epoch': 45, u'values': {u'loss': 0.24539561569690704, "
            "u'accumLoss': "
            "1170.0462956428528, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 78, u'type': u'duration', u'iteration': 743943}",
            "{u'name': u'LossDev', u'iteration': 922866, u'subtype': u'evaluation', u'epoch': 97, u'values': {u'loss': 0.19044341146945953, "
            "u'accumLoss': "
            "908.034185886383, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 113004, u'subtype': u'evaluation', u'epoch': 11, u'values': {u'loss': 0.3432103395462036, "
            "u'accumLoss': "
            "1636.4268989562988, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 4, u'iteration': 37668}",
            "{u'name': u'AccDev', u'iteration': 894615, u'subtype': u'evaluation', u'epoch': 94, u'values': {u'accumAccuracy': 4443.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9318372483221476}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 367263, u'subtype': u'train', u'epoch': 38, u'values': {u'accumAccuracy': 69392.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9211123647706909}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 122421, u'subtype': u'evaluation', u'epoch': 12, u'values': {u'truePositives': 25, "
            "u'numExamples': "
            "447, u'micro': {u'recall': 0.0992063492063492, u'precision': 0.11363636363636363, u'f': 0.1059322033898305}, u'macro': {u'recall': "
            "0.05893393393393393, u'precision': 0.051573426573426576, u'f': 0.05500855147512946}, u'perLabel': {u'truePositives': {u'1': 1, "
            "u'3': 24, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0.023529411764705885, u'3': 0.15189873417721517, u'2': 0, u'4': 0}, u'recall': {u'1': 0.013513513513513514, "
            "u'3': 0.2222222222222222, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0.09090909090909091, u'3': 0.11538461538461539, u'2': 0, "
            "u'4': 0.0}, "
            "u'falseNegatives': {u'1': 73, u'3': 84, u'2': 4, u'4': 66}, u'falsePositives': {u'1': 10, u'3': 184, u'4': 1}}, u'falseNegatives': 227, "
            "u'beta': 1.0, u'numLabels': 4, u'falsePositives': 25}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 725109, u'subtype': u'evaluation', u'epoch': 76, u'values': {u'loss': 0.20284733176231384, "
            "u'accumLoss': "
            "967.1760778427124, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 687441, u'subtype': u'train', u'epoch': 72, u'values': {u'loss': 0.16898406986870057, "
            "u'accumLoss': "
            "12730.414903558558, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 565020, u'subtype': u'evaluation', u'epoch': 59, u'values': {u'truePositives': 4400, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9228187919463087, u'precision': 0.9228187919463087, u'f': 0.9228187919463087}, u'macro': {u'recall': "
            "0.5074677346705877, "
            "u'precision': 0.4644042742806217, u'f': 0.48498193768302394}, u'perLabel': {u'truePositives': {u'0': 4075, u'3': 176, u'4': 149}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9759310262244042, u'3': 0.5761047463175123, u'2': 0, u'4': 0.8324022346368715}, u'recall': {u'1': 0.0, "
            "u'0': 0.9859666102105008, "
            "u'3': 0.775330396475771, u'2': 0.0, u'4': 0.7760416666666666}, u'precision': {u'1': 0, u'0': 0.9660976766239924, "
            "u'3': 0.4583333333333333, "
            "u'2': 0, u'4': 0.8975903614457831}, u'falseNegatives': {u'1': 119, u'0': 58, u'3': 51, u'2': 97, u'4': 43}, u'falsePositives': {u'0': "
            "143, "
            "u'3': 208, u'4': 17}}, u'falseNegatives': 368, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4400}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 856947, u'subtype': u'evaluation', u'epoch': 90, u'values': {u'accumAccuracy': 4441.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9314177852348994}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 29, u'iteration': 273093}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 87, u'type': u'duration', u'iteration': 828696}",
            "{u'name': u'LossTrain', u'iteration': 941700, u'subtype': u'train', u'epoch': 99, u'values': {u'loss': 0.14573701832904765, "
            "u'accumLoss': "
            "10979.098275818804, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 34, u'iteration': 320178}",
            "{u'name': u'LossTrain', u'iteration': 856947, u'subtype': u'train', u'epoch': 90, u'values': {u'loss': 0.15234616728422506, "
            "u'accumLoss': "
            "11476.998512357095, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 367263, u'subtype': u'evaluation', u'epoch': 38, u'values': {u'accumAccuracy': 4353.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9129614093959731}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 254259, u'subtype': u'evaluation', u'epoch': 26, u'values': {u'truePositives': 4282, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8980704697986577, u'precision': 0.8980704697986577, u'f': 0.8980704697986577}, u'macro': {u'recall': "
            "0.3769385944599767, "
            "u'precision': 0.4329705994654448, u'f': 0.4030163638814711}, u'perLabel': {u'truePositives': {u'0': 4088, u'3': 143, u'4': 51}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9672305690287472, u'3': 0.46504065040650405, u'2': 0, u'4': 0.4047619047619047}, u'recall': {u'1': 0.0, "
            "u'0': 0.9891120251633196, "
            "u'3': 0.6299559471365639, u'2': 0.0, u'4': 0.265625}, u'precision': {u'1': 0, u'0': 0.9462962962962963, u'3': 0.36855670103092786, "
            "u'2': 0, "
            "u'4': 0.85}, u'falseNegatives': {u'1': 119, u'0': 45, u'3': 84, u'2': 97, u'4': 141}, u'falsePositives': {u'0': 232, u'3': 245, "
            "u'4': 9}}, "
            "u'falseNegatives': 486, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4282}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 103587, u'subtype': u'evaluation', u'epoch': 10, u'values': {u'loss': 0.35092586278915405, "
            "u'accumLoss': "
            "1673.2145137786865, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 875781, u'subtype': u'train', u'epoch': 92, u'values': {u'loss': 0.15083787730433973, "
            "u'accumLoss': "
            "11363.371486722433, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 866364, u'subtype': u'train', u'epoch': 91, u'values': {u'loss': 0.15157421705726015, "
            "u'accumLoss': "
            "11418.843642008695, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 828696, u'subtype': u'evaluation', u'epoch': 87, u'values': {u'truePositives': 4436, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9303691275167785, u'precision': 0.9303691275167785, u'f': 0.9303691275167785}, u'macro': {u'recall': "
            "0.554352294057922, "
            "u'precision': 0.6259617533833406, u'f': 0.5879847566549316}, u'perLabel': {u'truePositives': {u'1': 18, u'0': 4076, u'3': 183, "
            "u'4': 159}, "
            "u'f': {u'1': 0.2535211267605634, u'0': 0.9780443911217757, u'3': 0.6235093696763203, u'2': 0, u'4': 0.8480000000000001}, "
            "u'recall': {u'1': "
            "0.15126050420168066, u'0': 0.9862085652068715, u'3': 0.8061674008810573, u'2': 0.0, u'4': 0.828125}, u'precision': {u'1': "
            "0.782608695652174, "
            "u'0': 0.9700142789148025, u'3': 0.5083333333333333, u'2': 0, u'4': 0.8688524590163934}, u'falseNegatives': {u'1': 101, u'0': 57, "
            "u'3': 44, "
            "u'2': 97, u'4': 33}, u'falsePositives': {u'1': 5, u'0': 126, u'3': 177, u'4': 24}}, u'falseNegatives': 332, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4436}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 743943, u'subtype': u'evaluation', u'epoch': 78, u'values': {u'truePositives': 4421, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9272231543624161, u'precision': 0.9272231543624161, u'f': 0.9272231543624161}, u'macro': {u'recall': "
            "0.5430331264508241, "
            "u'precision': 0.5861616753560701, u'f': 0.5637737734267284}, u'perLabel': {u'truePositives': {u'1': 11, u'0': 4067, u'3': 184, "
            "u'4': 159}, "
            "u'f': {u'1': 0.16058394160583941, u'0': 0.977409276616198, u'3': 0.6102819237147595, u'2': 0, u'4': 0.8435013262599469}, "
            "u'recall': {u'1': "
            "0.09243697478991597, u'0': 0.9840309702395355, u'3': 0.8105726872246696, u'2': 0.0, u'4': 0.828125}, u'precision': {u'1': "
            "0.6111111111111112, "
            "u'0': 0.9708761040821199, u'3': 0.48936170212765956, u'2': 0, u'4': 0.8594594594594595}, u'falseNegatives': {u'1': 108, u'0': 66, "
            "u'3': 43, "
            "u'2': 97, u'4': 33}, u'falsePositives': {u'1': 7, u'0': 122, u'3': 192, u'4': 26}}, u'falseNegatives': 347, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4421}, u'type': u'metric'}",
            u'Number of tokens read: 4768',
            "{u'name': u'LossTrain', u'iteration': 65919, u'subtype': u'train', u'epoch': 6, u'values': {u'loss': 0.39425490074037217, u'accumLoss': "
            "29701.192947275937, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 348429, u'subtype': u'train', u'epoch': 36, u'values': {u'accumAccuracy': 69295.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9198247826375523}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 536769, u'subtype': u'evaluation', u'epoch': 56, u'values': {u'loss': 0.22514212131500244, "
            "u'accumLoss': "
            "1073.4776344299316, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 87, u'type': u'duration', u'iteration': 828696}",
            "{u'name': u'AccTrain', u'iteration': 339012, u'subtype': u'train', u'epoch': 35, u'values': {u'accumAccuracy': 69231.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.918975243910533}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 37668, u'subtype': u'train', u'epoch': 3, u'values': {u'accumAccuracy': 65313.0, u'numExamples': "
            "75335, "
            "u'accuracy': 0.8669675449658193}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 725109, u'subtype': u'evaluation', u'epoch': 76, u'values': {u'accumAccuracy': 4419.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9268036912751678}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 348429, u'subtype': u'evaluation', u'epoch': 36, u'values': {u'truePositives': 75, "
            "u'numExamples': "
            "441, u'micro': {u'recall': 0.41208791208791207, u'precision': 0.2245508982035928, u'f': 0.29069767441860467}, u'macro': {u'recall': "
            "0.20896464646464646, u'precision': 0.12836597307221542, u'f': 0.15903655717914827}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 51, u'2': 0, "
            "u'4': 24}, u'f': {u'1': 0, u'3': 0.2786885245901639, u'2': 0, u'4': 0.3380281690140845}, u'recall': {u'1': 0.0, "
            "u'3': 0.4722222222222222, "
            "u'2': 0.0, u'4': 0.36363636363636365}, u'precision': {u'1': 0, u'3': 0.19767441860465115, u'2': 0, u'4': 0.3157894736842105}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 57, u'2': 4, u'4': 42}, u'falsePositives': {u'3': 207, u'4': 52}}, u'falseNegatives': 107, u'beta': 1.0, u'numLabels': "
            "4, "
            "u'falsePositives': 75}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 640356, u'subtype': u'evaluation', u'epoch': 67, u'values': {u'accumAccuracy': 4408.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.924496644295302}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 216591, u'subtype': u'evaluation', u'epoch': 22, u'values': {u'truePositives': 38, "
            "u'numExamples': "
            "421, u'micro': {u'recall': 0.2087912087912088, u'precision': 0.1371841155234657, u'f': 0.16557734204793031}, u'macro': {u'recall': "
            "0.08796296296296297, u'precision': 0.03725490196078431, u'f': 0.052341597796143245}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 38, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0, u'3': 0.20936639118457298, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.35185185185185186, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0.14901960784313725, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 4, u'3': 70, u'2': 4, u'4': 66}, "
            "u'falsePositives': {u'3': 217, u'4': 22}}, u'falseNegatives': 144, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 38}, "
            "u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 3, u'iteration': 28251}",
            "{u'name': u'CustomMetricDev', u'iteration': 339012, u'subtype': u'evaluation', u'epoch': 35, u'values': {u'truePositives': 77, "
            "u'numExamples': "
            "453, u'micro': {u'recall': 0.4230769230769231, u'precision': 0.22126436781609196, u'f': 0.29056603773584905}, u'macro': {u'recall': "
            "0.21064814814814814, u'precision': 0.1193993619087252, u'f': 0.15240990287616152}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 55, "
            "u'2': 0, "
            "u'4': 22}, u'f': {u'1': 0, u'3': 0.29333333333333333, u'2': 0, u'4': 0.2993197278911564}, u'recall': {u'1': 0.0, "
            "u'3': 0.5092592592592593, "
            "u'2': 0.0, u'4': 0.3333333333333333}, u'precision': {u'1': 0, u'3': 0.20599250936329588, u'2': 0, u'4': 0.2716049382716049}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 53, u'2': 4, u'4': 44}, u'falsePositives': {u'3': 212, u'4': 59}}, u'falseNegatives': 105, u'beta': 1.0, u'numLabels': "
            "4, "
            "u'falsePositives': 77}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 715692, u'subtype': u'evaluation', u'epoch': 75, u'values': {u'truePositives': 114, "
            "u'numExamples': "
            "446, u'micro': {u'recall': 0.4523809523809524, u'precision': 0.37012987012987014, u'f': 0.40714285714285714}, u'macro': {u'recall': "
            "0.3258372008372008, u'precision': 0.35102099842332657, u'f': 0.337960594069164}, u'perLabel': {u'truePositives': {u'1': 7, u'3': 70, "
            "u'2': 0, "
            "u'4': 37}, u'f': {u'1': 0.16279069767441862, u'3': 0.4229607250755287, u'2': 0, u'4': 0.5323741007194245}, u'recall': {u'1': "
            "0.0945945945945946, "
            "u'3': 0.6481481481481481, u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 0.5833333333333334, u'3': 0.31390134529147984, "
            "u'2': 0, "
            "u'4': 0.5068493150684932}, u'falseNegatives': {u'1': 67, u'3': 38, u'2': 4, u'4': 29}, u'falsePositives': {u'1': 5, u'3': 153, "
            "u'4': 36}}, "
            "u'falseNegatives': 138, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 114}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 169506, u'subtype': u'train', u'epoch': 17, u'values': {u'accumAccuracy': 67221.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.8922944182650826}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 197757, u'subtype': u'evaluation', u'epoch': 20, u'values': {u'truePositives': 38, "
            "u'numExamples': "
            "408, u'micro': {u'recall': 0.2087912087912088, u'precision': 0.14393939393939395, u'f': 0.17040358744394618}, u'macro': {u'recall': "
            "0.08796296296296297, u'precision': 0.038, u'f': 0.05307262569832402}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 38, u'2': 0, "
            "u'4': 0}, "
            "u'f': {u'1': 0, u'3': 0.2122905027932961, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.35185185185185186, u'2': 0.0, u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0.152, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 4, u'3': 70, u'2': 4, u'4': 66}, "
            "u'falsePositives': {u'3': "
            "212, u'4': 14}}, u'falseNegatives': 144, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 38}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 781611, u'subtype': u'evaluation', u'epoch': 82, u'values': {u'truePositives': 124, "
            "u'numExamples': "
            "447, u'micro': {u'recall': 0.49206349206349204, u'precision': 0.3887147335423197, u'f': 0.4343257443082311}, u'macro': {u'recall': "
            "0.3595413595413596, u'precision': 0.32173136003781166, u'f': 0.3395871499640833}, u'perLabel': {u'truePositives': {u'1': 10, u'3': 72, "
            "u'2': 0, "
            "u'4': 42}, u'f': {u'1': 0.20408163265306126, u'3': 0.44307692307692303, u'2': 0, u'4': 0.5833333333333334}, u'recall': {u'1': "
            "0.13513513513513514, "
            "u'3': 0.6666666666666666, u'2': 0.0, u'4': 0.6363636363636364}, u'precision': {u'1': 0.4166666666666667, u'3': 0.3317972350230415, "
            "u'2': 0, "
            "u'4': 0.5384615384615384}, u'falseNegatives': {u'1': 64, u'3': 36, u'2': 4, u'4': 24}, u'falsePositives': {u'1': 14, u'3': 145, "
            "u'4': 36}}, "
            "u'falseNegatives': 128, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 124}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 47085, u'subtype': u'train', u'epoch': 4, u'values': {u'accumAccuracy': 65309.0, u'numExamples': "
            "75335, "
            "u'accuracy': 0.8669144487953806}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 367263, u'subtype': u'evaluation', u'epoch': 38, u'values': {u'loss': 0.2615164816379547, "
            "u'accumLoss': "
            "1246.910584449768, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 433182, u'subtype': u'evaluation', u'epoch': 45, u'values': {u'truePositives': 93, "
            "u'numExamples': "
            "435, u'micro': {u'recall': 0.510989010989011, u'precision': 0.26878612716763006, u'f': 0.3522727272727273}, u'macro': {u'recall': "
            "0.2609427609427609, u'precision': 0.15322431633407244, u'f': 0.19307558877286116}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 62, "
            "u'2': 0, "
            "u'4': 31}, u'f': {u'1': 0, u'3': 0.33333333333333337, u'2': 0, u'4': 0.4189189189189189}, u'recall': {u'1': 0.0, "
            "u'3': 0.5740740740740741, "
            "u'2': 0.0, u'4': 0.4696969696969697}, u'precision': {u'1': 0, u'3': 0.23484848484848486, u'2': 0, u'4': 0.3780487804878049}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 46, u'2': 4, u'4': 35}, u'falsePositives': {u'3': 202, u'4': 51}}, u'falseNegatives': 89, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 93}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 10, u'iteration': 94170}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 92, u'type': u'duration', u'iteration': 875781}",
            "{u'learn_rate': [0.001], u'epoch': 62, u'iteration': 583854}",
            "{u'name': u'FMetricDev', u'iteration': 612105, u'subtype': u'evaluation', u'epoch': 64, u'values': {u'truePositives': 4402, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.923238255033557, u'precision': 0.923238255033557, u'f': 0.923238255033557}, u'macro': {u'recall': "
            "0.5091967979387694, "
            "u'precision': 0.6648858115986132, u'f': 0.5767187479155896}, u'perLabel': {u'truePositives': {u'1': 1, u'0': 4076, u'3': 176, "
            "u'4': 149}, "
            "u'f': {u'1': 0.016666666666666666, u'0': 0.9760536398467432, u'3': 0.5779967159277504, u'2': 0, u'4': 0.8324022346368715}, "
            "u'recall': {u'1': "
            "0.008403361344537815, u'0': 0.9862085652068715, u'3': 0.775330396475771, u'2': 0.0, u'4': 0.7760416666666666}, u'precision': {u'1': "
            "1.0, "
            "u'0': 0.9661057122540887, u'3': 0.4607329842931937, u'2': 0, u'4': 0.8975903614457831}, u'falseNegatives': {u'1': 118, u'0': 57, "
            "u'3': 51, "
            "u'2': 97, u'4': 43}, u'falsePositives': {u'0': 143, u'3': 206, u'4': 17}}, u'falseNegatives': 366, u'beta': 1.0, u'numLabels': 5, "
            "u'falsePositives': 4402}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 659190, u'subtype': u'train', u'epoch': 69, u'values': {u'accumAccuracy': 70523.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9361253069622354}, u'type': u'metric'}",
            u'Normalizing word embedding: minmax',
            "{u'name': u'AccTrain', u'iteration': 875781, u'subtype': u'train', u'epoch': 92, u'values': {u'accumAccuracy': 71111.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9439304440167253}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 282510, u'subtype': u'train', u'epoch': 29, u'values': {u'accumAccuracy': 68632.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9110240923873366}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 41, u'type': u'duration', u'iteration': 395514}",
            "{u'name': u'AccDev', u'iteration': 743943, u'subtype': u'evaluation', u'epoch': 78, u'values': {u'accumAccuracy': 4421.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9272231543624161}, u'type': u'metric'}",
            u'Reading development examples',
            "{u'name': u'LossDev', u'iteration': 461433, u'subtype': u'evaluation', u'epoch': 48, u'values': {u'loss': 0.23908184468746185, "
            "u'accumLoss': "
            "1139.9422354698181, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 26, u'type': u'duration', u'iteration': 254259}",
            "{u'learn_rate': [0.001], u'epoch': 61, u'iteration': 574437}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 14, u'type': u'duration', u'iteration': 141255}",
            "{u'name': u'AccDev', u'iteration': 913449, u'subtype': u'evaluation', u'epoch': 96, u'values': {u'accumAccuracy': 4449.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9330956375838926}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 941700, u'subtype': u'evaluation', u'epoch': 99, u'values': {u'truePositives': 143, "
            "u'numExamples': "
            "472, u'micro': {u'recall': 0.46885245901639344, u'precision': 0.4612903225806452, u'f': 0.46504065040650405}, u'macro': {u'recall': "
            "0.42854756670546146, u'precision': 0.5491949152542372, u'f': 0.4814276743043606}, u'perLabel': {u'truePositives': {u'1': 26, u'3': 72, "
            "u'2': 6, "
            "u'4': 39}, u'f': {u'1': 0.4193548387096775, u'3': 0.5052631578947367, u'2': 0.1846153846153846, u'4': 0.5531914893617023}, "
            "u'recall': {u'1': "
            "0.35135135135135137, u'3': 0.6666666666666666, u'2': 0.10526315789473684, u'4': 0.5909090909090909}, u'precision': {u'1': 0.52, "
            "u'3': 0.4067796610169492, u'2': 0.75, u'4': 0.52}, u'falseNegatives': {u'1': 48, u'3': 36, u'2': 51, u'4': 27}, u'falsePositives': {"
            "u'1': 24, "
            "u'3': 105, u'2': 2, u'4': 36}}, u'falseNegatives': 162, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 143}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 809862, u'subtype': u'train', u'epoch': 85, u'values': {u'accumAccuracy': 70963.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9419658857104931}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 169506, u'subtype': u'train', u'epoch': 17, u'values': {u'loss': 0.2975391523798691, "
            "u'accumLoss': "
            "22415.11204453744, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 565020, u'subtype': u'evaluation', u'epoch': 59, u'values': {u'truePositives': 105, "
            "u'numExamples': "
            "399, u'micro': {u'recall': 0.5769230769230769, u'precision': 0.32608695652173914, u'f': 0.41666666666666663}, u'macro': {u'recall': "
            "0.29903198653198654, u'precision': 0.2005358846304921, u'f': 0.24007406165838824}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 67, "
            "u'2': 0, "
            "u'4': 38}, u'f': {u'1': 0, u'3': 0.37325905292479106, u'2': 0, u'4': 0.5547445255474452}, u'recall': {u'1': 0.0, "
            "u'3': 0.6203703703703703, "
            "u'2': 0.0, u'4': 0.5757575757575758}, u'precision': {u'1': 0, u'3': 0.26693227091633465, u'2': 0, u'4': 0.5352112676056338}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 41, u'2': 4, u'4': 28}, u'falsePositives': {u'3': 184, u'4': 33}}, u'falseNegatives': 77, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 105}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 263676, u'subtype': u'train', u'epoch': 27, u'values': {u'accumAccuracy': 68374.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.90759938939404}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 517935, u'subtype': u'evaluation', u'epoch': 54, u'values': {u'accumAccuracy': 4391.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9209312080536913}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 762777, u'subtype': u'evaluation', u'epoch': 80, u'values': {u'truePositives': 4423, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9276426174496645, u'precision': 0.9276426174496645, u'f': 0.9276426174496645}, u'macro': {u'recall': "
            "0.5449558503862134, "
            "u'precision': 0.5858028342198022, u'f': 0.5646415738865385}, u'perLabel': {u'truePositives': {u'1': 11, u'0': 4067, u'3': 185, "
            "u'4': 160}, "
            "u'f': {u'1': 0.16058394160583941, u'0': 0.9777617502103619, u'3': 0.6125827814569537, u'2': 0, u'4': 0.8443271767810027}, "
            "u'recall': {u'1': "
            "0.09243697478991597, u'0': 0.9840309702395355, u'3': 0.8149779735682819, u'2': 0.0, u'4': 0.8333333333333334}, u'precision': {u'1': "
            "0.6111111111111112, u'0': 0.9715719063545151, u'3': 0.4907161803713528, u'2': 0, u'4': 0.8556149732620321}, u'falseNegatives': {u'1': "
            "108, "
            "u'0': 66, u'3': 42, u'2': 97, u'4': 32}, u'falsePositives': {u'1': 7, u'0': 119, u'3': 192, u'4': 27}}, u'falseNegatives': 345, "
            "u'beta': 1.0, "
            "u'numLabels': 5, u'falsePositives': 4423}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 480267, u'subtype': u'train', u'epoch': 50, u'values': {u'loss': 0.20337492616500175, "
            "u'accumLoss': "
            "15321.250062640407, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 94170, u'subtype': u'evaluation', u'epoch': 9, u'values': {u'loss': 0.3579626679420471, "
            "u'accumLoss': "
            "1706.7660007476807, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 357846, u'subtype': u'evaluation', u'epoch': 37, u'values': {u'truePositives': 4349, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9121224832214765, u'precision': 0.9121224832214765, u'f': 0.9121224832214765}, u'macro': {u'recall': "
            "0.45044138355977975, "
            "u'precision': 0.4403235505449133, u'f': 0.4453250048976314}, u'perLabel': {u'truePositives': {u'0': 4082, u'3': 157, u'4': 110}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9723677941877084, u'3': 0.5250836120401338, u'2': 0, u'4': 0.6748466257668712}, u'recall': {u'1': 0.0, "
            "u'0': 0.9876602951850956, "
            "u'3': 0.6916299559471366, u'2': 0.0, u'4': 0.5729166666666666}, u'precision': {u'1': 0, u'0': 0.957541637344593, "
            "u'3': 0.42318059299191374, "
            "u'2': 0, u'4': 0.8208955223880597}, u'falseNegatives': {u'1': 119, u'0': 51, u'3': 70, u'2': 97, u'4': 82}, u'falsePositives': {u'0': "
            "181, "
            "u'3': 214, u'4': 24}}, u'falseNegatives': 419, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4349}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 828696, u'subtype': u'train', u'epoch': 87, u'values': {u'loss': 0.1547010741985434, "
            "u'accumLoss': "
            "11654.405424747267, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 715692, u'subtype': u'train', u'epoch': 75, u'values': {u'accumAccuracy': 70707.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9385677308024158}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 348429, u'subtype': u'evaluation', u'epoch': 36, u'values': {u'truePositives': 4346, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9114932885906041, u'precision': 0.9114932885906041, u'f': 0.9114932885906041}, u'macro': {u'recall': "
            "0.4462934886126598, "
            "u'precision': 0.44162778528909785, u'f': 0.4439483786639432}, u'perLabel': {u'truePositives': {u'0': 4084, u'3': 151, u'4': 111}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9709938183547313, u'3': 0.5189003436426116, u'2': 0, u'4': 0.6809815950920245}, u'recall': {u'1': 0.0, u'0': 0.988144205177837, "
            "u'3': 0.6651982378854625, u'2': 0.0, u'4': 0.578125}, u'precision': {u'1': 0, u'0': 0.9544286048142089, u'3': 0.4253521126760563, "
            "u'2': 0, "
            "u'4': 0.8283582089552238}, u'falseNegatives': {u'1': 119, u'0': 49, u'3': 76, u'2': 97, u'4': 81}, u'falsePositives': {u'0': 195, "
            "u'3': 204, "
            "u'4': 23}}, u'falseNegatives': 422, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4346}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 60, u'type': u'duration', u'iteration': 574437}", u'Loading label lexicon...',
            "{u'name': u'AccDev', u'iteration': 301344, u'subtype': u'evaluation', u'epoch': 31, u'values': {u'accumAccuracy': 4324.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9068791946308725}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 461433, u'subtype': u'evaluation', u'epoch': 48, u'values': {u'accumAccuracy': 4377.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.917994966442953}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 60, u'type': u'duration', u'iteration': 574437}",
            "{u'learn_rate': [0.001], u'epoch': 60, u'iteration': 565020}",
            "{u'name': u'LossTrain', u'iteration': 517935, u'subtype': u'train', u'epoch': 54, u'values': {u'loss': 0.1954177581207303, "
            "u'accumLoss': "
            "14721.796808025218, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 74, u'iteration': 696858}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 54, u'type': u'duration', u'iteration': 517935}", u'BatchSize: 9223372036854775807',
            "{u'name': u'LossTrain', u'iteration': 160089, u'subtype': u'train', u'epoch': 16, u'values': {u'loss': 0.3018530921956394, "
            "u'accumLoss': "
            "22740.10270055849, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 14, u'subtype': u'training', u'epoch': 9, u'type': u'duration', u'iteration': 94170}",
            "{u'name': u'AccDev', u'iteration': 423765, u'subtype': u'evaluation', u'epoch': 44, u'values': {u'accumAccuracy': 4366.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9156879194630873}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 23, u'type': u'duration', u'iteration': 226008}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 38, u'type': u'duration', u'iteration': 367263}",
            "{u'name': u'AccTrain', u'iteration': 329595, u'subtype': u'train', u'epoch': 34, u'values': {u'accumAccuracy': 69169.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.918152253268733}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 46, u'type': u'duration', u'iteration': 442599}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 83, u'type': u'duration', u'iteration': 791028}",
            "{u'learn_rate': [0.001], u'epoch': 32, u'iteration': 301344}",
            "{u'name': u'CustomMetricDev', u'iteration': 555603, u'subtype': u'evaluation', u'epoch': 58, u'values': {u'truePositives': 104, "
            "u'numExamples': "
            "405, u'micro': {u'recall': 0.5714285714285714, u'precision': 0.3180428134556575, u'f': 0.4086444007858546}, u'macro': {u'recall': "
            "0.2952441077441077, u'precision': 0.19415849673202612, u'f': 0.23426173708227482}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 67, "
            "u'2': 0, "
            "u'4': 37}, u'f': {u'1': 0, u'3': 0.36914600550964183, u'2': 0, u'4': 0.5362318840579711}, u'recall': {u'1': 0.0, "
            "u'3': 0.6203703703703703, "
            "u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 0, u'3': 0.2627450980392157, u'2': 0, u'4': 0.5138888888888888}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 41, u'2': 4, u'4': 29}, u'falsePositives': {u'3': 188, u'4': 35}}, u'falseNegatives': 78, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 104}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 913449, u'subtype': u'train', u'epoch': 96, u'values': {u'accumAccuracy': 71240.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9456427955133736}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 12, u'type': u'duration', u'iteration': 122421}",
            "{u'name': u'LossTrain', u'iteration': 706275, u'subtype': u'train', u'epoch': 74, u'values': {u'loss': 0.16680745081438678, "
            "u'accumLoss': "
            "12566.439307101828, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 75, u'iteration': 706275}",
            "{u'name': u'LossDev', u'iteration': 565020, u'subtype': u'evaluation', u'epoch': 59, u'values': {u'loss': 0.22052885591983795, "
            "u'accumLoss': "
            "1051.4815850257874, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 480267, u'subtype': u'evaluation', u'epoch': 50, u'values': {u'truePositives': 98, "
            "u'numExamples': "
            "428, u'micro': {u'recall': 0.5384615384615384, u'precision': 0.28488372093023256, u'f': 0.3726235741444867}, u'macro': {u'recall': "
            "0.27546296296296297, u'precision': 0.16575113446381656, u'f': 0.20696663538250834}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 65, u'2': 0, "
            "u'4': 33}, u'f': {u'1': 0, u'3': 0.34852546916890087, u'2': 0, u'4': 0.45517241379310347}, u'recall': {u'1': 0.0, "
            "u'3': 0.6018518518518519, "
            "u'2': 0.0, u'4': 0.5}, u'precision': {u'1': 0, u'3': 0.24528301886792453, u'2': 0, u'4': 0.4177215189873418}, u'falseNegatives': {"
            "u'1': 4, "
            "u'3': 43, u'2': 4, u'4': 33}, u'falsePositives': {u'3': 200, u'4': 46}}, u'falseNegatives': 84, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': "
            "98}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 47, u'type': u'duration', u'iteration': 452016}",
            "{u'name': u'AccTrain', u'iteration': 791028, u'subtype': u'train', u'epoch': 83, u'values': {u'accumAccuracy': 70890.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9409968805999868}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 197757, u'subtype': u'evaluation', u'epoch': 20, u'values': {u'loss': 0.3075856566429138, "
            "u'accumLoss': "
            "1466.568410873413, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 367263, u'subtype': u'train', u'epoch': 38, u'values': {u'loss': 0.23234579981236528, "
            "u'accumLoss': "
            "17503.770828864537, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 122421, u'subtype': u'evaluation', u'epoch': 12, u'values': {u'accumAccuracy': 4192.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8791946308724832}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 489684, u'subtype': u'train', u'epoch': 51, u'values': {u'accumAccuracy': 69949.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9285060065042808}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 442599, u'subtype': u'evaluation', u'epoch': 46, u'values': {u'truePositives': 92, "
            "u'numExamples': "
            "434, u'micro': {u'recall': 0.5054945054945055, u'precision': 0.26744186046511625, u'f': 0.3498098859315589}, u'macro': {u'recall': "
            "0.25862794612794615, u'precision': 0.15271830199218023, u'f': 0.1920388041018453}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 61, "
            "u'2': 0, "
            "u'4': 31}, u'f': {u'1': 0, u'3': 0.32972972972972975, u'2': 0, u'4': 0.4189189189189189}, u'recall': {u'1': 0.0, "
            "u'3': 0.5648148148148148, "
            "u'2': 0.0, u'4': 0.4696969696969697}, u'precision': {u'1': 0, u'3': 0.23282442748091603, u'2': 0, u'4': 0.3780487804878049}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 47, u'2': 4, u'4': 35}, u'falsePositives': {u'3': 201, u'4': 51}}, u'falseNegatives': 90, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 92}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 517935, u'subtype': u'evaluation', u'epoch': 54, u'values': {u'truePositives': 4391, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9209312080536913, u'precision': 0.9209312080536913, u'f': 0.9209312080536913}, u'macro': {u'recall': "
            "0.5038917792769987, "
            "u'precision': 0.4519406862840246, u'f': 0.4765044183881325}, u'perLabel': {u'truePositives': {u'0': 4069, u'3': 177, u'4': 145}, "
            "u'f': {u'1': 0, "
            "u'0': 0.976481881449484, u'3': 0.5691318327974276, u'2': 0, u'4': 0.7967032967032968}, u'recall': {u'1': 0.0, u'0': 0.9845148802322768, "
            "u'3': 0.7797356828193832, u'2': 0.0, u'4': 0.7552083333333334}, u'precision': {u'1': 0, u'0': 0.9685789097833849, "
            "u'3': 0.4481012658227848, "
            "u'2': 0, u'4': 0.8430232558139535}, u'falseNegatives': {u'1': 119, u'0': 64, u'3': 50, u'2': 97, u'4': 47}, u'falsePositives': {u'0': "
            "132, "
            "u'3': 218, u'4': 27}}, u'falseNegatives': 377, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4391}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 263676, u'subtype': u'train', u'epoch': 27, u'values': {u'loss': 0.26361704886435205, "
            "u'accumLoss': "
            "19859.590376195963, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 725109, u'subtype': u'evaluation', u'epoch': 76, u'values': {u'truePositives': 4419, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9268036912751678, u'precision': 0.9268036912751678, u'f': 0.9268036912751678}, u'macro': {u'recall': "
            "0.5366589036415682, "
            "u'precision': 0.6078048124256535, u'f': 0.5700204553191118}, u'perLabel': {u'truePositives': {u'1': 10, u'0': 4071, u'3': 182, "
            "u'4': 156}, "
            "u'f': {u'1': 0.15037593984962405, u'0': 0.9768446310737854, u'3': 0.6076794657762938, u'2': 0, u'4': 0.8387096774193549}, "
            "u'recall': {u'1': "
            "0.08403361344537816, u'0': 0.9849987902250181, u'3': 0.801762114537445, u'2': 0.0, u'4': 0.8125}, u'precision': {u'1': "
            "0.7142857142857143, "
            "u'0': 0.9688243693479296, u'3': 0.489247311827957, u'2': 0, u'4': 0.8666666666666667}, u'falseNegatives': {u'1': 109, u'0': 62, "
            "u'3': 45, "
            "u'2': 97, u'4': 36}, u'falsePositives': {u'1': 4, u'0': 131, u'3': 190, u'4': 24}}, u'falseNegatives': 349, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4419}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 169506, u'subtype': u'evaluation', u'epoch': 17, u'values': {u'loss': 0.31680652499198914, "
            "u'accumLoss': "
            "1510.5335111618042, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 499101, u'subtype': u'evaluation', u'epoch': 52, u'values': {u'accumAccuracy': 4386.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9198825503355704}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 141255, u'subtype': u'evaluation', u'epoch': 14, u'values': {u'loss': 0.3279183804988861, "
            "u'accumLoss': "
            "1563.514838218689, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 508518, u'subtype': u'train', u'epoch': 53, u'values': {u'loss': 0.19730844288849023, "
            "u'accumLoss': "
            "14864.231545004412, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 602688, u'subtype': u'evaluation', u'epoch': 63, u'values': {u'loss': 0.21519434452056885, "
            "u'accumLoss': "
            "1026.0466346740723, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 33, u'type': u'duration', u'iteration': 320178}",
            "{u'learn_rate': [0.001], u'epoch': 8, u'iteration': 75336}",
            "{u'name': u'CustomMetricDev', u'iteration': 188340, u'subtype': u'evaluation', u'epoch': 19, u'values': {u'truePositives': 37, "
            "u'numExamples': "
            "407, u'micro': {u'recall': 0.2032967032967033, u'precision': 0.14122137404580154, u'f': 0.16666666666666669}, u'macro': {u'recall': "
            "0.08564814814814815, u'precision': 0.037, u'f': 0.051675977653631286}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 37, u'2': 0, "
            "u'4': 0}, "
            "u'f': {u'1': 0, u'3': 0.20670391061452514, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.3425925925925926, u'2': 0.0, u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0.148, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 4, u'3': 71, u'2': 4, u'4': 66}, "
            "u'falsePositives': {u'3': "
            "213, u'4': 12}}, u'falseNegatives': 145, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 37}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 678024, u'subtype': u'evaluation', u'epoch': 71, u'values': {u'loss': 0.2072034478187561, "
            "u'accumLoss': "
            "987.9460391998291, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 207174, u'subtype': u'train', u'epoch': 21, u'values': {u'loss': 0.28251348805128035, "
            "u'accumLoss': "
            "21283.153622343205, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 0, u'type': u'duration', u'iteration': 9417}",
            "{u'name': u'LossDev', u'iteration': 395514, u'subtype': u'evaluation', u'epoch': 41, u'values': {u'loss': 0.25474610924720764, "
            "u'accumLoss': "
            "1214.629448890686, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 226008, u'subtype': u'train', u'epoch': 23, u'values': {u'loss': 0.2759485091414497, "
            "u'accumLoss': "
            "20788.580936171114, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 178923, u'subtype': u'train', u'epoch': 18, u'values': {u'loss': 0.2935027228869345, "
            "u'accumLoss': "
            "22111.02762868721, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 131838, u'subtype': u'evaluation', u'epoch': 13, u'values': {u'truePositives': 28, "
            "u'numExamples': "
            "461, u'micro': {u'recall': 0.1111111111111111, u'precision': 0.11814345991561181, u'f': 0.11451942740286299}, u'macro': {u'recall': "
            "0.06587837837837837, u'precision': 0.07922077922077922, u'f': 0.0719361374013486}, u'perLabel': {u'truePositives': {u'1': 1, u'3': 27, "
            "u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0.02531645569620253, u'3': 0.1592920353982301, u'2': 0, u'4': 0}, u'recall': {u'1': 0.013513513513513514, "
            "u'3': 0.25, "
            "u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0.2, u'3': 0.11688311688311688, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 73, "
            "u'3': 81, u'2': 4, "
            "u'4': 66}, u'falsePositives': {u'1': 4, u'3': 204, u'4': 1}}, u'falseNegatives': 224, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 28}, "
            "u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 414348, u'subtype': u'evaluation', u'epoch': 43, u'values': {u'accumAccuracy': 4361.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9146392617449665}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 10, u'type': u'duration', u'iteration': 103587}",
            "{u'name': u'LossDev', u'iteration': 838113, u'subtype': u'evaluation', u'epoch': 88, u'values': {u'loss': 0.1946531981229782, "
            "u'accumLoss': "
            "928.1064486503601, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 904032, u'subtype': u'evaluation', u'epoch': 95, u'values': {u'truePositives': 4448, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9328859060402684, u'precision': 0.9328859060402684, u'f': 0.9328859060402684}, u'macro': {u'recall': "
            "0.5850495023689604, "
            "u'precision': 0.6747939643326347, u'f': 0.6267252773362119}, u'perLabel': {u'truePositives': {u'1': 34, u'0': 4069, u'3': 183, u'2': 1, "
            "u'4': 161}, u'f': {u'1': 0.40236686390532544, u'0': 0.977654973570399, u'3': 0.6547406082289803, u'2': 0.02, u'4': 0.8385416666666666}, "
            "u'recall': {u'1': 0.2857142857142857, u'0': 0.9845148802322768, u'3': 0.8061674008810573, u'2': 0.010309278350515464, "
            "u'4': 0.8385416666666666}, "
            "u'precision': {u'1': 0.68, u'0': 0.9708900023860654, u'3': 0.5512048192771084, u'2': 0.3333333333333333, u'4': 0.8385416666666666}, "
            "u'falseNegatives': {u'1': 85, u'0': 64, u'3': 44, u'2': 96, u'4': 31}, u'falsePositives': {u'1': 16, u'0': 122, u'3': 149, u'2': 2, "
            "u'4': 31}}, "
            "u'falseNegatives': 320, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4448}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 273093, u'subtype': u'evaluation', u'epoch': 28, u'values': {u'truePositives': 4300, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9018456375838926, u'precision': 0.9018456375838926, u'f': 0.9018456375838926}, u'macro': {u'recall': "
            "0.39687209880504076, "
            "u'precision': 0.4359396700860116, u'f': 0.41548954585449854}, u'perLabel': {u'truePositives': {u'0': 4086, u'3': 148, u'4': 66}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9684759421663901, u'3': 0.4836601307189543, u'2': 0, u'4': 0.4888888888888889}, u'recall': {u'1': 0.0, "
            "u'0': 0.9886281151705782, "
            "u'3': 0.6519823788546255, u'2': 0.0, u'4': 0.34375}, u'precision': {u'1': 0, u'0': 0.9491289198606272, u'3': 0.38441558441558443, "
            "u'2': 0, "
            "u'4': 0.8461538461538461}, u'falseNegatives': {u'1': 119, u'0': 47, u'3': 79, u'2': 97, u'4': 126}, u'falsePositives': {u'0': 219, "
            "u'3': 237, "
            "u'4': 12}}, u'falseNegatives': 468, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4300}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 89, u'type': u'duration', u'iteration': 847530}",
            "{u'name': u'AccTrain', u'iteration': 470850, u'subtype': u'train', u'epoch': 49, u'values': {u'accumAccuracy': 69856.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9272715205415809}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 527352, u'subtype': u'evaluation', u'epoch': 55, u'values': {u'accumAccuracy': 4393.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9213506711409396}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 762777, u'subtype': u'train', u'epoch': 80, u'values': {u'accumAccuracy': 70850.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9404659188955996}, u'type': u'metric'}",
            "{u'duration': 6, u'subtype': u'training', u'epoch': 57, u'type': u'duration', u'iteration': 546186}",
            "{u'name': u'FMetricDev', u'iteration': 838113, u'subtype': u'evaluation', u'epoch': 88, u'values': {u'truePositives': 4446, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9324664429530202, u'precision': 0.9324664429530202, u'f': 0.9324664429530202}, u'macro': {u'recall': "
            "0.5645637891299373, "
            "u'precision': 0.609858971513609, u'f': 0.5863379071501337}, u'perLabel': {u'truePositives': {u'1': 26, u'0': 4082, u'3': 179, "
            "u'4': 159}, "
            "u'f': {u'1': 0.3291139240506329, u'0': 0.977841657683555, u'3': 0.6415770609318997, u'2': 0, u'4': 0.8502673796791443}, "
            "u'recall': {u'1': "
            "0.2184873949579832, u'0': 0.9876602951850956, u'3': 0.788546255506608, u'2': 0.0, u'4': 0.828125}, u'precision': {u'1': "
            "0.6666666666666666, "
            "u'0': 0.9682163187855788, u'3': 0.540785498489426, u'2': 0, u'4': 0.8736263736263736}, u'falseNegatives': {u'1': 93, u'0': 51, "
            "u'3': 48, u'2': 97, "
            "u'4': 33}, u'falsePositives': {u'1': 13, u'0': 134, u'3': 152, u'4': 23}}, u'falseNegatives': 322, u'beta': 1.0, u'numLabels': 5, "
            "u'falsePositives': 4446}, u'type': u'metric'}",
            u'Usando o filtro: data.Filters TransformNumberToZeroFilter',
            "{u'name': u'AccDev', u'iteration': 442599, u'subtype': u'evaluation', u'epoch': 46, u'values': {u'accumAccuracy': 4371.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.916736577181208}, u'type': u'metric'}",
            u'Done!',
            "{u'name': u'LossTrain', u'iteration': 743943, u'subtype': u'train', u'epoch': 78, u'values': {u'loss': 0.1626766337690832, "
            "u'accumLoss': "
            "12255.244204993884, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 442599, u'subtype': u'evaluation', u'epoch': 46, u'values': {u'truePositives': 4371, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.916736577181208, u'precision': 0.916736577181208, u'f': 0.916736577181208}, u'macro': {u'recall': "
            "0.4768789439819113, "
            "u'precision': 0.44309702050921845, u'f': 0.4593677386753178}, u'perLabel': {u'truePositives': {u'0': 4077, u'3': 166, u'4': 128}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9744263862332696, u'3': 0.5514950166112957, u'2': 0, u'4': 0.7314285714285714}, u'recall': {u'1': 0.0, "
            "u'0': 0.9864505202032422, "
            "u'3': 0.7312775330396476, u'2': 0.0, u'4': 0.6666666666666666}, u'precision': {u'1': 0, u'0': 0.9626918536009446, "
            "u'3': 0.44266666666666665, "
            "u'2': 0, u'4': 0.810126582278481}, u'falseNegatives': {u'1': 119, u'0': 56, u'3': 61, u'2': 97, u'4': 64}, u'falsePositives': {u'0': "
            "158, "
            "u'3': 209, u'4': 30}}, u'falseNegatives': 397, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4371}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 696858, u'subtype': u'evaluation', u'epoch': 73, u'values': {u'truePositives': 4414, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.925755033557047, u'precision': 0.925755033557047, u'f': 0.925755033557047}, u'macro': {u'recall': "
            "0.5244099977561413, "
            "u'precision': 0.6367195960900899, u'f': 0.5751332559716225}, u'perLabel': {u'truePositives': {u'1': 6, u'0': 4076, u'3': 179, "
            "u'4': 153}, "
            "u'f': {u'1': 0.09523809523809523, u'0': 0.9766383131664071, u'3': 0.5966666666666667, u'2': 0, u'4': 0.8360655737704917}, "
            "u'recall': {u'1': "
            "0.05042016806722689, u'0': 0.9862085652068715, u'3': 0.788546255506608, u'2': 0.0, u'4': 0.796875}, u'precision': {u'1': "
            "0.8571428571428571, "
            "u'0': 0.9672520170859041, u'3': 0.47989276139410186, u'2': 0, u'4': 0.8793103448275862}, u'falseNegatives': {u'1': 113, u'0': 57, "
            "u'3': 48, "
            "u'2': 97, u'4': 39}, u'falsePositives': {u'1': 1, u'0': 138, u'3': 194, u'4': 21}}, u'falseNegatives': 354, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4414}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 72, u'type': u'duration', u'iteration': 687441}",
            "{u'learn_rate': [0.001], u'epoch': 56, u'iteration': 527352}",
            "{u'name': u'AccTrain', u'iteration': 941700, u'subtype': u'train', u'epoch': 99, u'values': {u'accumAccuracy': 71341.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9469834738169509}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 263676, u'subtype': u'evaluation', u'epoch': 27, u'values': {u'truePositives': 49, "
            "u'numExamples': "
            "470, u'micro': {u'recall': 0.2692307692307692, u'precision': 0.14540059347181009, u'f': 0.18882466281310212}, u'macro': {u'recall': "
            "0.11637205387205388, u'precision': 0.050843454790823216, u'f': 0.07076804427139326}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 47, u'2': 0, "
            "u'4': 2}, u'f': {u'1': 0, u'3': 0.23918575063613232, u'2': 0, u'4': 0.03389830508474576}, u'recall': {u'1': 0.0, "
            "u'3': 0.4351851851851852, "
            "u'2': 0.0, u'4': 0.030303030303030304}, u'precision': {u'1': 0, u'3': 0.1649122807017544, u'2': 0, u'4': 0.038461538461538464}, "
            "u'falseNegatives': "
            "{u'1': 4, u'3': 61, u'2': 4, u'4': 64}, u'falsePositives': {u'3': 238, u'4': 50}}, u'falseNegatives': 133, u'beta': 1.0, "
            "u'numLabels': 4, "
            "u'falsePositives': 49}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 97, u'iteration': 913449}",
            "{u'name': u'CustomMetricDev', u'iteration': 668607, u'subtype': u'evaluation', u'epoch': 70, u'values': {u'truePositives': 112, "
            "u'numExamples': "
            "455, u'micro': {u'recall': 0.4444444444444444, u'precision': 0.35555555555555557, u'f': 0.3950617283950617}, u'macro': {u'recall': "
            "0.32014400764400763, u'precision': 0.41585115684691953, u'f': 0.36177481146484025}, u'perLabel': {u'truePositives': {u'1': 6, "
            "u'3': 69, u'2': 0, "
            "u'4': 37}, u'f': {u'1': 0.14814814814814817, u'3': 0.4011627906976744, u'2': 0, u'4': 0.5362318840579711}, u'recall': {u'1': "
            "0.08108108108108109, "
            "u'3': 0.6388888888888888, u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 0.8571428571428571, u'3': 0.2923728813559322, "
            "u'2': 0, "
            "u'4': 0.5138888888888888}, u'falseNegatives': {u'1': 68, u'3': 39, u'2': 4, u'4': 29}, u'falsePositives': {u'1': 1, u'3': 167, "
            "u'4': 35}}, "
            "u'falseNegatives': 140, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 112}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 62, u'type': u'duration', u'iteration': 593271}",
            "{u'name': u'AccTrain', u'iteration': 555603, u'subtype': u'train', u'epoch': 58, u'values': {u'accumAccuracy': 70191.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9317183248158226}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 310761, u'subtype': u'evaluation', u'epoch': 32, u'values': {u'loss': 0.27724766731262207, "
            "u'accumLoss': "
            "1321.916877746582, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 76, u'type': u'duration', u'iteration': 725109}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 9, u'type': u'duration', u'iteration': 94170}",
            "{u'name': u'CustomMetricDev', u'iteration': 621522, u'subtype': u'evaluation', u'epoch': 65, u'values': {u'truePositives': 104, "
            "u'numExamples': "
            "455, u'micro': {u'recall': 0.4126984126984127, u'precision': 0.33876221498371334, u'f': 0.37209302325581395}, u'macro': {u'recall': "
            "0.2963076713076713, u'precision': 0.32735562310030397, u'f': 0.31105881407498914}, u'perLabel': {u'truePositives': {u'1': 1, u'3': 66, "
            "u'2': 0, "
            "u'4': 37}, u'f': {u'1': 0.026315789473684213, u'3': 0.38483965014577265, u'2': 0, u'4': 0.5441176470588236}, u'recall': {u'1': "
            "0.013513513513513514, u'3': 0.6111111111111112, u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 0.5, "
            "u'3': 0.28085106382978725, "
            "u'2': 0, u'4': 0.5285714285714286}, u'falseNegatives': {u'1': 73, u'3': 42, u'2': 4, u'4': 29}, u'falsePositives': {u'1': 1, u'3': 169, "
            "u'4': 33}}, u'falseNegatives': 148, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 104}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 65919, u'subtype': u'evaluation', u'epoch': 6, u'values': {u'accumAccuracy': 4154.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8712248322147651}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 329595, u'subtype': u'train', u'epoch': 34, u'values': {u'loss': 0.2434753412727426, "
            "u'accumLoss': "
            "18342.214834782062, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 348429, u'subtype': u'evaluation', u'epoch': 36, u'values': {u'accumAccuracy': 4346.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9114932885906041}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 630939, u'subtype': u'evaluation', u'epoch': 66, u'values': {u'truePositives': 4401, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9230285234899329, u'precision': 0.9230285234899329, u'f': 0.9230285234899329}, u'macro': {u'recall': "
            "0.5180514046872289, "
            "u'precision': 0.6089233767386221, u'f': 0.5598237260770312}, u'perLabel': {u'truePositives': {u'1': 3, u'0': 4067, u'3': 178, "
            "u'4': 153}, "
            "u'f': {u'1': 0.04878048780487805, u'0': 0.9758848230353929, u'3': 0.5816993464052287, u'2': 0, u'4': 0.8292682926829269}, "
            "u'recall': {u'1': "
            "0.025210084033613446, u'0': 0.9840309702395355, u'3': 0.7841409691629956, u'2': 0.0, u'4': 0.796875}, u'precision': {u'1': 0.75, "
            "u'0': 0.9678724416944312, u'3': 0.4623376623376623, u'2': 0, u'4': 0.864406779661017}, u'falseNegatives': {u'1': 116, u'0': 66, "
            "u'3': 49, "
            "u'2': 97, u'4': 39}, u'falsePositives': {u'1': 1, u'0': 135, u'3': 207, u'4': 24}}, u'falseNegatives': 367, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4401}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 141255, u'subtype': u'evaluation', u'epoch': 14, u'values': {u'truePositives': 4205, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8819211409395973, u'precision': 0.8819211409395973, u'f': 0.8819211409395973}, u'macro': {u'recall': "
            "0.29024205336830844, "
            "u'precision': 0.44506120944049227, u'f': 0.35135293377905347}, u'perLabel': {u'truePositives': {u'0': 4101, u'3': 103, u'4': 1}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9588496609773205, u'3': 0.35951134380453753, u'2': 0, u'4': 0.010362694300518135}, u'recall': {u'1': 0.0, "
            "u'0': 0.9922574401161384, "
            "u'3': 0.45374449339207046, u'2': 0.0, u'4': 0.005208333333333333}, u'precision': {u'1': 0, u'0': 0.9276181859307849, "
            "u'3': 0.2976878612716763, "
            "u'2': 0, u'4': 1.0}, u'falseNegatives': {u'1': 119, u'0': 32, u'3': 124, u'2': 97, u'4': 191}, u'falsePositives': {u'0': 320, "
            "u'3': 243}}, "
            "u'falseNegatives': 563, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4205}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 461433, u'subtype': u'train', u'epoch': 48, u'values': {u'accumAccuracy': 69829.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9269131213911197}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 452016, u'subtype': u'evaluation', u'epoch': 47, u'values': {u'truePositives': 93, "
            "u'numExamples': "
            "421, u'micro': {u'recall': 0.510989010989011, u'precision': 0.28012048192771083, u'f': 0.36186770428015563}, u'macro': {u'recall': "
            "0.2609427609427609, u'precision': 0.16252055921052633, u'f': 0.2002939164365166}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 62, "
            "u'2': 0, "
            "u'4': 31}, u'f': {u'1': 0, u'3': 0.34065934065934067, u'2': 0, u'4': 0.43661971830985913}, u'recall': {u'1': 0.0, "
            "u'3': 0.5740740740740741, "
            "u'2': 0.0, u'4': 0.4696969696969697}, u'precision': {u'1': 0, u'3': 0.2421875, u'2': 0, u'4': 0.40789473684210525}, u'falseNegatives': "
            "{u'1': 4, "
            "u'3': 46, u'2': 4, u'4': 35}, u'falsePositives': {u'3': 194, u'4': 45}}, u'falseNegatives': 89, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': "
            "93}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 828696, u'subtype': u'evaluation', u'epoch': 87, u'values': {u'truePositives': 123, "
            "u'numExamples': "
            "434, u'micro': {u'recall': 0.4880952380952381, u'precision': 0.40327868852459015, u'f': 0.44165170556552963}, u'macro': {u'recall': "
            "0.3549344799344799, u'precision': 0.34873000090391393, u'f': 0.3518048867861168}, u'perLabel': {u'truePositives': {u'1': 12, u'3': 72, "
            "u'2': 0, "
            "u'4': 39}, u'f': {u'1': 0.24742268041237114, u'3': 0.45569620253164556, u'2': 0, u'4': 0.5571428571428572}, u'recall': {u'1': "
            "0.16216216216216217, "
            "u'3': 0.6666666666666666, u'2': 0.0, u'4': 0.5909090909090909}, u'precision': {u'1': 0.5217391304347826, u'3': 0.34615384615384615, "
            "u'2': 0, "
            "u'4': 0.527027027027027}, u'falseNegatives': {u'1': 62, u'3': 36, u'2': 4, u'4': 27}, u'falsePositives': {u'1': 11, u'3': 136, "
            "u'4': 35}}, "
            "u'falseNegatives': 129, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 123}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 678024, u'subtype': u'evaluation', u'epoch': 71, u'values': {u'accumAccuracy': 4412.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9253355704697986}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 23, u'type': u'duration', u'iteration': 226008}",
            "{u'name': u'CustomMetricDev', u'iteration': 489684, u'subtype': u'evaluation', u'epoch': 51, u'values': {u'truePositives': 97, "
            "u'numExamples': "
            "419, u'micro': {u'recall': 0.532967032967033, u'precision': 0.2904191616766467, u'f': 0.375968992248062}, u'macro': {u'recall': "
            "0.27462121212121215, u'precision': 0.17288861689106488, u'f': 0.21219145795021888}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 63, u'2': 0, "
            "u'4': 34}, u'f': {u'1': 0, u'3': 0.3442622950819672, u'2': 0, u'4': 0.4788732394366197}, u'recall': {u'1': 0.0, "
            "u'3': 0.5833333333333334, "
            "u'2': 0.0, u'4': 0.5151515151515151}, u'precision': {u'1': 0, u'3': 0.2441860465116279, u'2': 0, u'4': 0.4473684210526316}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 45, u'2': 4, u'4': 32}, u'falsePositives': {u'3': 195, u'4': 42}}, u'falseNegatives': 85, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 97}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 63, u'iteration': 593271}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 49, u'type': u'duration', u'iteration': 470850}",
            "{u'name': u'FMetricDev', u'iteration': 423765, u'subtype': u'evaluation', u'epoch': 44, u'values': {u'truePositives': 4366, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9156879194630873, u'precision': 0.9156879194630873, u'f': 0.9156879194630873}, u'macro': {u'recall': "
            "0.4686907836464004, "
            "u'precision': 0.44724271747953165, u'f': 0.4577156299621075}, u'perLabel': {u'truePositives': {u'0': 4080, u'3': 166, u'4': 120}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9740957383311447, u'3': 0.5460526315789473, u'2': 0, u'4': 0.7164179104477612}, u'recall': {u'1': 0.0, "
            "u'0': 0.9871763851923542, "
            "u'3': 0.7312775330396476, u'2': 0.0, u'4': 0.625}, u'precision': {u'1': 0, u'0': 0.9613572101790764, u'3': 0.4356955380577428, u'2': 0, "
            "u'4': 0.8391608391608392}, u'falseNegatives': {u'1': 119, u'0': 53, u'3': 61, u'2': 97, u'4': 72}, u'falsePositives': {u'0': 164, "
            "u'3': 215, "
            "u'4': 23}}, u'falseNegatives': 402, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4366}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 593271, u'subtype': u'evaluation', u'epoch': 62, u'values': {u'truePositives': 105, "
            "u'numExamples': "
            "471, u'micro': {u'recall': 0.4166666666666667, u'precision': 0.32407407407407407, u'f': 0.3645833333333334}, u'macro': {u'recall': "
            "0.2986224861224861, u'precision': 0.44520528995130587, u'f': 0.3574706801671037}, u'perLabel': {u'truePositives': {u'1': 1, u'3': 67, "
            "u'2': 0, "
            "u'4': 37}, u'f': {u'1': 0.026666666666666665, u'3': 0.37325905292479106, u'2': 0, u'4': 0.5362318840579711}, u'recall': {u'1': "
            "0.013513513513513514, u'3': 0.6203703703703703, u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 1.0, "
            "u'3': 0.26693227091633465, "
            "u'2': 0, u'4': 0.5138888888888888}, u'falseNegatives': {u'1': 73, u'3': 41, u'2': 4, u'4': 29}, u'falsePositives': {u'1': 0, u'3': 184, "
            "u'4': 35}}, u'falseNegatives': 147, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 105}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 602688, u'subtype': u'evaluation', u'epoch': 63, u'values': {u'truePositives': 106, "
            "u'numExamples': "
            "464, u'micro': {u'recall': 0.42063492063492064, u'precision': 0.3333333333333333, u'f': 0.3719298245614035}, u'macro': {u'recall': "
            "0.3024103649103649, u'precision': 0.4518922477957174, u'f': 0.3623397221595385}, u'perLabel': {u'truePositives': {u'1': 1, u'3': 67, "
            "u'2': 0, "
            "u'4': 38}, u'f': {u'1': 0.026666666666666665, u'3': 0.3785310734463277, u'2': 0, u'4': 0.5547445255474452}, u'recall': {u'1': "
            "0.013513513513513514, u'3': 0.6203703703703703, u'2': 0.0, u'4': 0.5757575757575758}, u'precision': {u'1': 1.0, "
            "u'3': 0.27235772357723576, "
            "u'2': 0, u'4': 0.5352112676056338}, u'falseNegatives': {u'1': 73, u'3': 41, u'2': 4, u'4': 28}, u'falsePositives': {u'1': 0, u'3': 179, "
            "u'4': 33}}, u'falseNegatives': 146, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 106}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 17, u'type': u'duration', u'iteration': 169506}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 37, u'type': u'duration', u'iteration': 357846}",
            "{u'name': u'CustomMetricDev', u'iteration': 527352, u'subtype': u'evaluation', u'epoch': 55, u'values': {u'truePositives': 100, "
            "u'numExamples': "
            "413, u'micro': {u'recall': 0.5494505494505495, u'precision': 0.3021148036253776, u'f': 0.38986354775828463}, u'macro': {u'recall': "
            "0.28303872053872053, u'precision': 0.18147281522767905, u'f': 0.221152025212276}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 65, "
            "u'2': 0, "
            "u'4': 35}, u'f': {u'1': 0, u'3': 0.3561643835616438, u'2': 0, u'4': 0.5}, u'recall': {u'1': 0.0, u'3': 0.6018518518518519, u'2': 0.0, "
            "u'4': 0.5303030303030303}, u'precision': {u'1': 0, u'3': 0.2529182879377432, u'2': 0, u'4': 0.47297297297297297}, u'falseNegatives': {"
            "u'1': 4, "
            "u'3': 43, u'2': 4, u'4': 31}, u'falsePositives': {u'3': 192, u'4': 39}}, u'falseNegatives': 82, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': "
            "100}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 28251, u'subtype': u'evaluation', u'epoch': 2, u'values': {u'truePositives': 0, "
            "u'numExamples': 16, "
            "u'micro': {u'recall': 0.0, u'precision': 0, u'f': 0}, u'macro': {u'recall': 0.0, u'precision': 0.0, u'f': 0}, u'perLabel': {"
            "u'truePositives': {"
            "u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'f': {u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.0, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'falseNegatives': {u'1': 4, u'3': 4, u'2': 4, u'4': 4}, u'falsePositives': {}}, "
            "u'falseNegatives': 16, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 0}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 875781, u'subtype': u'evaluation', u'epoch': 92, u'values': {u'truePositives': 135, "
            "u'numExamples': "
            "427, u'micro': {u'recall': 0.5357142857142857, u'precision': 0.43548387096774194, u'f': 0.48042704626334526}, u'macro': {u'recall': "
            "0.39629402129402125, u'precision': 0.35455532839253767, u'f': 0.37426457629231746}, u'perLabel': {u'truePositives': {u'1': 22, "
            "u'3': 72, u'2': 0, "
            "u'4': 41}, u'f': {u'1': 0.37606837606837606, u'3': 0.4848484848484849, u'2': 0, u'4': 0.5694444444444445}, u'recall': {u'1': "
            "0.2972972972972973, "
            "u'3': 0.6666666666666666, u'2': 0.0, u'4': 0.6212121212121212}, u'precision': {u'1': 0.5116279069767442, u'3': 0.38095238095238093, "
            "u'2': 0, "
            "u'4': 0.5256410256410257}, u'falseNegatives': {u'1': 52, u'3': 36, u'2': 4, u'4': 25}, u'falsePositives': {u'1': 21, u'3': 117, "
            "u'4': 37}}, "
            "u'falseNegatives': 117, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 135}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 84, u'iteration': 791028}",
            "{u'name': u'AccDev', u'iteration': 9417, u'subtype': u'evaluation', u'epoch': 0, u'values': {u'accumAccuracy': 4133.0, u'numExamples': "
            "4768, "
            "u'accuracy': 0.8668204697986577}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 31, u'type': u'duration', u'iteration': 301344}",
            "{u'name': u'AccTrain', u'iteration': 56502, u'subtype': u'train', u'epoch': 5, u'values': {u'accumAccuracy': 65359.0, u'numExamples': "
            "75335, "
            "u'accuracy': 0.8675781509258644}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 244842, u'subtype': u'train', u'epoch': 25, u'values': {u'loss': 0.2696583614686063, "
            "u'accumLoss': "
            "20314.712661237456, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 96, u'type': u'duration', u'iteration': 913449}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 93, u'type': u'duration', u'iteration': 885198}",
            "{u'name': u'LossDev', u'iteration': 160089, u'subtype': u'evaluation', u'epoch': 16, u'values': {u'loss': 0.32094472646713257, "
            "u'accumLoss': "
            "1530.264455795288, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 46, u'iteration': 433182}",
            "{u'name': u'LossTrain', u'iteration': 103587, u'subtype': u'train', u'epoch': 10, u'values': {u'loss': 0.3390144837533003, "
            "u'accumLoss': "
            "25539.656133554876, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 546186, u'subtype': u'evaluation', u'epoch': 57, u'values': {u'truePositives': 103, "
            "u'numExamples': "
            "404, u'micro': {u'recall': 0.5659340659340659, u'precision': 0.3169230769230769, u'f': 0.40631163708086787}, u'macro': {u'recall': "
            "0.29440235690235694, u'precision': 0.19462111328549686, u'f': 0.23433196133592857}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 65, u'2': 0, "
            "u'4': 38}, u'f': {u'1': 0, u'3': 0.36111111111111116, u'2': 0, u'4': 0.5467625899280576}, u'recall': {u'1': 0.0, "
            "u'3': 0.6018518518518519, "
            "u'2': 0.0, u'4': 0.5757575757575758}, u'precision': {u'1': 0, u'3': 0.25793650793650796, u'2': 0, u'4': 0.5205479452054794}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 43, u'2': 4, u'4': 28}, u'falsePositives': {u'3': 187, u'4': 35}}, u'falseNegatives': 79, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 103}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 56502, u'subtype': u'evaluation', u'epoch': 5, u'values': {u'truePositives': 2, "
            "u'numExamples': 322, "
            "u'micro': {u'recall': 0.007936507936507936, u'precision': 0.027777777777777776, u'f': 0.012345679012345678}, u'macro': {u'recall': "
            "0.005693193193193193, u'precision': 0.014474772539288668, u'f': 0.008172135711335021}, u'perLabel': {u'truePositives': {u'1': 1, "
            "u'3': 1, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0.017699115044247787, u'3': 0.014388489208633093, u'2': 0, u'4': 0}, u'recall': {u'1': 0.013513513513513514, "
            "u'3': 0.009259259259259259, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0.02564102564102564, u'3': 0.03225806451612903, u'2': 0, "
            "u'4': 0.0}, "
            "u'falseNegatives': {u'1': 73, u'3': 107, u'2': 4, u'4': 66}, u'falsePositives': {u'1': 38, u'3': 30, u'4': 2}}, u'falseNegatives': 250, "
            "u'beta': 1.0, u'numLabels': 4, u'falsePositives': 2}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 17, u'iteration': 160089}",
            "{u'name': u'LossTrain', u'iteration': 847530, u'subtype': u'train', u'epoch': 89, u'values': {u'loss': 0.15315054441570208, "
            "u'accumLoss': "
            "11537.596263556916, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 71, u'type': u'duration', u'iteration': 678024}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 74, u'type': u'duration', u'iteration': 706275}",
            "{u'name': u'FMetricDev', u'iteration': 367263, u'subtype': u'evaluation', u'epoch': 38, u'values': {u'truePositives': 4353, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9129614093959731, u'precision': 0.9129614093959731, u'f': 0.9129614093959731}, u'macro': {u'recall': "
            "0.45460805022644646, "
            "u'precision': 0.44076682041518966, u'f': 0.44758045239725736}, u'perLabel': {u'truePositives': {u'0': 4082, u'3': 157, u'4': 114}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9727153580364589, u'3': 0.5268456375838926, u'2': 0, u'4': 0.6888217522658611}, u'recall': {u'1': 0.0, "
            "u'0': 0.9876602951850956, "
            "u'3': 0.6916299559471366, u'2': 0.0, u'4': 0.59375}, u'precision': {u'1': 0, u'0': 0.9582159624413146, u'3': 0.4254742547425474, "
            "u'2': 0, "
            "u'4': 0.8201438848920863}, u'falseNegatives': {u'1': 119, u'0': 51, u'3': 70, u'2': 97, u'4': 78}, u'falsePositives': {u'0': 178, "
            "u'3': 212, "
            "u'4': 25}}, u'falseNegatives': 415, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4353}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 226008, u'subtype': u'evaluation', u'epoch': 23, u'values': {u'accumAccuracy': 4254.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8921979865771812}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 75336, u'subtype': u'evaluation', u'epoch': 7, u'values': {u'truePositives': 4158, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8720637583892618, u'precision': 0.8720637583892618, u'f': 0.8720637583892618}, u'macro': {u'recall': "
            "0.2390031929336165, "
            "u'precision': 0.4411056379339769, u'f': 0.3100258402842736}, u'perLabel': {u'truePositives': {u'1': 3, u'0': 4118, u'3': 24, u'4': 13}, "
            "u'f': {u'1': 0.03636363636363636, u'0': 0.9417953116066323, u'3': 0.14814814814814817, u'2': 0, u'4': 0.12682926829268293}, "
            "u'recall': {u'1': "
            "0.025210084033613446, u'0': 0.9963706750544399, u'3': 0.10572687224669604, u'2': 0.0, u'4': 0.06770833333333333}, u'precision': {u'1': "
            "0.06521739130434782, u'0': 0.8928881179531657, u'3': 0.24742268041237114, u'2': 0, u'4': 1.0}, u'falseNegatives': {u'1': 116, "
            "u'0': 15, u'3': 203, "
            "u'2': 97, u'4': 179}, u'falsePositives': {u'1': 43, u'0': 494, u'3': 73}}, u'falseNegatives': 610, u'beta': 1.0, u'numLabels': 5, "
            "u'falsePositives': 4158}, u'type': u'metric'}",
            u'Compiling the network...',
            "{u'name': u'AccTrain', u'iteration': 649773, u'subtype': u'train', u'epoch': 68, u'values': {u'accumAccuracy': 70489.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9356739895135063}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 75336, u'subtype': u'evaluation', u'epoch': 7, u'values': {u'loss': 0.3799084722995758, "
            "u'accumLoss': "
            "1811.4035959243774, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 706275, u'subtype': u'evaluation', u'epoch': 74, u'values': {u'accumAccuracy': 4418.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9265939597315436}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 800445, u'subtype': u'train', u'epoch': 84, u'values': {u'accumAccuracy': 70947.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9417535010287383}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 33, u'iteration': 310761}", "{u'learn_rate': [0.001], u'epoch': 70, u'iteration': 659190}",
            "{u'name': u'FMetricDev', u'iteration': 188340, u'subtype': u'evaluation', u'epoch': 19, u'values': {u'truePositives': 4221, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8852768456375839, u'precision': 0.8852768456375839, u'f': 0.8852768456375839}, u'macro': {u'recall': "
            "0.3157764494827457, "
            "u'precision': 0.41630844821888424, u'f': 0.3591397775884978}, u'perLabel': {u'truePositives': {u'0': 4089, u'3': 122, u'4': 10}, "
            "u'f': {u'1': 0, "
            "u'0': 0.962457337883959, u'3': 0.394184168012924, u'2': 0, u'4': 0.09803921568627451}, u'recall': {u'1': 0.0, u'0': 0.9893539801596903, "
            "u'3': 0.5374449339207048, u'2': 0.0, u'4': 0.052083333333333336}, u'precision': {u'1': 0, u'0': 0.9369844179651695, "
            "u'3': 0.3112244897959184, "
            "u'2': 0, u'4': 0.8333333333333334}, u'falseNegatives': {u'1': 119, u'0': 44, u'3': 105, u'2': 97, u'4': 182}, u'falsePositives': {"
            "u'0': 275, "
            "u'3': 270, u'4': 2}}, u'falseNegatives': 547, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4221}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 574437, u'subtype': u'evaluation', u'epoch': 60, u'values': {u'loss': 0.21891474723815918, "
            "u'accumLoss': "
            "1043.785514831543, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 9417, u'subtype': u'train', u'epoch': 0, u'values': {u'loss': 0.5636829932517534, u'accumLoss': "
            "42465.058296620846, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 583854, u'subtype': u'train', u'epoch': 61, u'values': {u'accumAccuracy': 70278.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9328731665228646}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 734526, u'subtype': u'train', u'epoch': 77, u'values': {u'loss': 0.16368410297283809, "
            "u'accumLoss': "
            "12331.141897458758, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 23, u'iteration': 216591}",
            "{u'name': u'CustomMetricDev', u'iteration': 922866, u'subtype': u'evaluation', u'epoch': 97, u'values': {u'truePositives': 144, "
            "u'numExamples': "
            "485, u'micro': {u'recall': 0.4721311475409836, u'precision': 0.4444444444444444, u'f': 0.4578696343402226}, u'macro': {u'recall': "
            "0.42718555876450615, u'precision': 0.4770597681888004, u'f': 0.45074724206636}, u'perLabel': {u'truePositives': {u'1': 27, u'3': 74, "
            "u'2': 3, "
            "u'4': 40}, u'f': {u'1': 0.4186046511627907, u'3': 0.5034013605442177, u'2': 0.09523809523809525, u'4': 0.5594405594405594}, "
            "u'recall': {u'1': "
            "0.36486486486486486, u'3': 0.6851851851851852, u'2': 0.05263157894736842, u'4': 0.6060606060606061}, u'precision': {u'1': "
            "0.4909090909090909, "
            "u'3': 0.3978494623655914, u'2': 0.5, u'4': 0.5194805194805194}, u'falseNegatives': {u'1': 47, u'3': 34, u'2': 54, u'4': 26}, "
            "u'falsePositives': {"
            "u'1': 28, u'3': 112, u'2': 3, u'4': 37}}, u'falseNegatives': 161, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 144}, "
            "u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 320178, u'subtype': u'train', u'epoch': 33, u'values': {u'accumAccuracy': 69092.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9171301519877879}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 20, u'type': u'duration', u'iteration': 197757}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 17, u'type': u'duration', u'iteration': 169506}",
            "{u'learn_rate': [0.001], u'epoch': 38, u'iteration': 357846}",
            "{u'duration': 14, u'subtype': u'training', u'epoch': 6, u'type': u'duration', u'iteration': 65919}",
            "{u'name': u'AccDev', u'iteration': 875781, u'subtype': u'evaluation', u'epoch': 92, u'values': {u'accumAccuracy': 4446.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9324664429530202}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 339012, u'subtype': u'train', u'epoch': 35, u'values': {u'loss': 0.24065357391646966, "
            "u'accumLoss': "
            "18129.63699099724, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 574437, u'subtype': u'evaluation', u'epoch': 60, u'values': {u'truePositives': 105, "
            "u'numExamples': "
            "396, u'micro': {u'recall': 0.5769230769230769, u'precision': 0.329153605015674, u'f': 0.4191616766467065}, u'macro': {u'recall': "
            "0.29903198653198654, u'precision': 0.2029833620195066, u'f': 0.24181937127130856}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 67, "
            "u'2': 0, "
            "u'4': 38}, u'f': {u'1': 0, u'3': 0.3753501400560224, u'2': 0, u'4': 0.5588235294117646}, u'recall': {u'1': 0.0, "
            "u'3': 0.6203703703703703, "
            "u'2': 0.0, u'4': 0.5757575757575758}, u'precision': {u'1': 0, u'3': 0.26907630522088355, u'2': 0, u'4': 0.5428571428571428}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 41, u'2': 4, u'4': 28}, u'falsePositives': {u'3': 182, u'4': 32}}, u'falseNegatives': 77, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 105}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 35, u'iteration': 329595}",
            "{u'duration': 14, u'subtype': u'training', u'epoch': 1, u'type': u'duration', u'iteration': 18834}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 68, u'type': u'duration', u'iteration': 649773}",
            "{u'name': u'CustomMetricDev', u'iteration': 141255, u'subtype': u'evaluation', u'epoch': 14, u'values': {u'truePositives': 27, "
            "u'numExamples': "
            "379, u'micro': {u'recall': 0.14835164835164835, u'precision': 0.12053571428571429, u'f': 0.1330049261083744}, u'macro': {u'recall': "
            "0.0625, "
            "u'precision': 0.030269058295964126, u'f': 0.04078549848942598}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 27, u'2': 0, u'4': 0}, "
            "u'f': {u'1': 0, u'3': 0.16314199395770393, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.25, u'2': 0.0, u'4': 0.0}, u'precision': "
            "{u'1': 0, "
            "u'3': 0.1210762331838565, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 4, u'3': 81, u'2': 4, u'4': 66}, u'falsePositives': {u'3': "
            "196, "
            "u'4': 1}}, u'falseNegatives': 155, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 27}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 27, u'type': u'duration', u'iteration': 263676}",
            "{u'duration': 14, u'subtype': u'training', u'epoch': 0, u'type': u'duration', u'iteration': 9417}",
            "{u'name': u'AccDev', u'iteration': 536769, u'subtype': u'evaluation', u'epoch': 56, u'values': {u'accumAccuracy': 4397.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9221895973154363}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 508518, u'subtype': u'evaluation', u'epoch': 53, u'values': {u'loss': 0.22947856783866882, "
            "u'accumLoss': "
            "1094.153811454773, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 30, u'iteration': 282510}",
            "{u'name': u'FMetricDev', u'iteration': 819279, u'subtype': u'evaluation', u'epoch': 86, u'values': {u'truePositives': 4427, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.928481543624161, u'precision': 0.928481543624161, u'f': 0.928481543624161}, u'macro': {u'recall': "
            "0.5543040963988696, "
            "u'precision': 0.5909948787538818, u'f': 0.5720617748747018}, u'perLabel': {u'truePositives': {u'1': 16, u'0': 4065, u'3': 185, "
            "u'4': 161}, "
            "u'f': {u'1': 0.22222222222222224, u'0': 0.9782216339790639, u'3': 0.6156405990016639, u'2': 0, u'4': 0.8429319371727747}, "
            "u'recall': {u'1': "
            "0.13445378151260504, u'0': 0.9835470602467941, u'3': 0.8149779735682819, u'2': 0.0, u'4': 0.8385416666666666}, u'precision': {u'1': "
            "0.64, "
            "u'0': 0.9729535662996649, u'3': 0.4946524064171123, u'2': 0.0, u'4': 0.8473684210526315}, u'falseNegatives': {u'1': 103, u'0': 68, "
            "u'3': 42, "
            "u'2': 97, u'4': 31}, u'falsePositives': {u'1': 9, u'0': 113, u'3': 189, u'2': 1, u'4': 29}}, u'falseNegatives': 341, u'beta': 1.0, "
            "u'numLabels': "
            "5, u'falsePositives': 4427}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 913449, u'subtype': u'train', u'epoch': 96, u'values': {u'loss': 0.14791252972169838, "
            "u'accumLoss': "
            "11142.990426584147, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 72, u'iteration': 678024}",
            "{u'name': u'LossDev', u'iteration': 894615, u'subtype': u'evaluation', u'epoch': 94, u'values': {u'loss': 0.19209420680999756, "
            "u'accumLoss': "
            "915.9051780700684, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 26, u'iteration': 244842}",
            "{u'name': u'LossDev', u'iteration': 235425, u'subtype': u'evaluation', u'epoch': 24, u'values': {u'loss': 0.2978106141090393, "
            "u'accumLoss': "
            "1419.9610080718994, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 254259, u'subtype': u'evaluation', u'epoch': 26, u'values': {u'accumAccuracy': 4282.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8980704697986577}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 52, u'type': u'duration', u'iteration': 499101}",
            "{u'name': u'FMetricDev', u'iteration': 678024, u'subtype': u'evaluation', u'epoch': 71, u'values': {u'truePositives': 4412, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9253355704697986, u'precision': 0.9253355704697986, u'f': 0.9253355704697986}, u'macro': {u'recall': "
            "0.5261391576944339, "
            "u'precision': 0.635248791696379, u'f': 0.5755686794664164}, u'perLabel': {u'truePositives': {u'1': 6, u'0': 4072, u'3': 180, "
            "u'4': 154}, "
            "u'f': {u'1': 0.09523809523809523, u'0': 0.9764988009592326, u'3': 0.5950413223140495, u'2': 0, u'4': 0.8369565217391305}, "
            "u'recall': {u'1': "
            "0.05042016806722689, u'0': 0.9852407452213888, u'3': 0.7929515418502202, u'2': 0.0, u'4': 0.8020833333333334}, u'precision': {u'1': "
            "0.8571428571428571, u'0': 0.967910625148562, u'3': 0.47619047619047616, u'2': 0, u'4': 0.875}, u'falseNegatives': {u'1': 113, "
            "u'0': 61, u'3': 47, "
            "u'2': 97, u'4': 38}, u'falsePositives': {u'1': 1, u'0': 135, u'3': 198, u'4': 22}}, u'falseNegatives': 356, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4412}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 18834, u'subtype': u'evaluation', u'epoch': 1, u'values': {u'loss': 0.5173563957214355, "
            "u'accumLoss': "
            "2466.7552947998047, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 18834, u'subtype': u'evaluation', u'epoch': 1, u'values': {u'accumAccuracy': 4133.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8668204697986577}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 16, u'iteration': 150672}", "{u'learn_rate': [0.001], u'epoch': 98, u'iteration': 922866}",
            "{u'name': u'AccTrain', u'iteration': 565020, u'subtype': u'train', u'epoch': 59, u'values': {u'accumAccuracy': 70226.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9321829163071613}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 414348, u'subtype': u'train', u'epoch': 43, u'values': {u'loss': 0.2191844208736096, "
            "u'accumLoss': "
            "16512.25834651338, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 433182, u'subtype': u'evaluation', u'epoch': 45, u'values': {u'truePositives': 4372, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9169463087248322, u'precision': 0.9169463087248322, u'f': 0.9169463087248322}, u'macro': {u'recall': "
            "0.4777600012506338, "
            "u'precision': 0.44324882180491326, u'f': 0.45985782624166116}, u'perLabel': {u'truePositives': {u'0': 4077, u'3': 167, u'4': 128}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9746593354052115, u'3': 0.5529801324503312, u'2': 0, u'4': 0.7314285714285714}, u'recall': {u'1': 0.0, "
            "u'0': 0.9864505202032422, "
            "u'3': 0.73568281938326, u'2': 0.0, u'4': 0.6666666666666666}, u'precision': {u'1': 0, u'0': 0.9631467044649185, "
            "u'3': 0.44297082228116713, "
            "u'2': 0, u'4': 0.810126582278481}, u'falseNegatives': {u'1': 119, u'0': 56, u'3': 60, u'2': 97, u'4': 64}, u'falsePositives': {u'0': "
            "156, "
            "u'3': 210, u'4': 30}}, u'falseNegatives': 396, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4372}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 404931, u'subtype': u'evaluation', u'epoch': 42, u'values': {u'accumAccuracy': 4357.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9138003355704698}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 141255, u'subtype': u'train', u'epoch': 14, u'values': {u'loss': 0.31161316247054766, "
            "u'accumLoss': "
            "23475.37759471871, u'numExamples': 75335}, u'type': u'metric'}",
            u'Number of batches: 1',
            "{u'name': u'AccTrain', u'iteration': 687441, u'subtype': u'train', u'epoch': 72, u'values': {u'accumAccuracy': 70589.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.937001393774474}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 22, u'type': u'duration', u'iteration': 216591}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 69, u'type': u'duration', u'iteration': 659190}",
            "{u'name': u'AccTrain', u'iteration': 856947, u'subtype': u'train', u'epoch': 90, u'values': {u'accumAccuracy': 71077.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9434791265679963}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 37668, u'subtype': u'evaluation', u'epoch': 3, u'values': {u'truePositives': 0, "
            "u'numExamples': 202, "
            "u'micro': {u'recall': 0.0, u'precision': 0.0, u'f': 0}, u'macro': {u'recall': 0.0, u'precision': 0.0, u'f': 0}, u'perLabel': {"
            "u'truePositives': {"
            "u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'f': {u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.0, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0.0, u'3': 0.0, u'2': 0, u'4': 0}, u'falseNegatives': {u'1': 74, u'3': 108, u'2': 4, u'4': 4}, u'falsePositives': "
            "{u'1': 2, "
            "u'3': 10}}, u'falseNegatives': 190, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 0}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 612105, u'subtype': u'evaluation', u'epoch': 64, u'values': {u'accumAccuracy': 4402.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.923238255033557}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 90, u'iteration': 847530}",
            "{u'name': u'CustomMetricDev', u'iteration': 395514, u'subtype': u'evaluation', u'epoch': 41, u'values': {u'truePositives': 88, "
            "u'numExamples': "
            "450, u'micro': {u'recall': 0.4835164835164835, u'precision': 0.24719101123595505, u'f': 0.3271375464684015}, u'macro': {u'recall': "
            "0.24494949494949497, u'precision': 0.13848039215686275, u'f': 0.17693301049233254}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 60, u'2': 0, "
            "u'4': 28}, u'f': {u'1': 0, u'3': 0.31578947368421056, u'2': 0, u'4': 0.3733333333333333}, u'recall': {u'1': 0.0, "
            "u'3': 0.5555555555555556, "
            "u'2': 0.0, u'4': 0.42424242424242425}, u'precision': {u'1': 0, u'3': 0.22058823529411764, u'2': 0, u'4': 0.3333333333333333}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 48, u'2': 4, u'4': 38}, u'falsePositives': {u'3': 212, u'4': 56}}, u'falseNegatives': 94, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 88}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 649773, u'subtype': u'evaluation', u'epoch': 68, u'values': {u'truePositives': 108, "
            "u'numExamples': "
            "465, u'micro': {u'recall': 0.42857142857142855, u'precision': 0.3364485981308411, u'f': 0.37696335078534027}, u'macro': {u'recall': "
            "0.30769405769405767, u'precision': 0.38245884773662553, u'f': 0.34102678938267694}, u'perLabel': {u'truePositives': {u'1': 3, "
            "u'3': 68, u'2': 0, "
            "u'4': 37}, u'f': {u'1': 0.07692307692307693, u'3': 0.3874643874643875, u'2': 0, u'4': 0.5285714285714286}, u'recall': {u'1': "
            "0.04054054054054054, "
            "u'3': 0.6296296296296297, u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 0.75, u'3': 0.27983539094650206, u'2': 0, "
            "u'4': 0.5}, "
            "u'falseNegatives': {u'1': 71, u'3': 40, u'2': 4, u'4': 29}, u'falsePositives': {u'1': 1, u'3': 175, u'4': 37}}, u'falseNegatives': 144, "
            "u'beta': 1.0, u'numLabels': 4, u'falsePositives': 108}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 753360, u'subtype': u'evaluation', u'epoch': 79, u'values': {u'truePositives': 115, "
            "u'numExamples': "
            "442, u'micro': {u'recall': 0.45634920634920634, u'precision': 0.3770491803278688, u'f': 0.4129263913824058}, u'macro': {u'recall': "
            "0.3302791427791427, u'precision': 0.3098086124401914, u'f': 0.3197165454517395}, u'perLabel': {u'truePositives': {u'1': 9, u'3': 69, "
            "u'2': 0, "
            "u'4': 37}, u'f': {u'1': 0.1875, u'3': 0.43533123028391163, u'2': 0, u'4': 0.5285714285714286}, u'recall': {u'1': 0.12162162162162163, "
            "u'3': 0.6388888888888888, u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 0.4090909090909091, u'3': 0.33014354066985646, "
            "u'2': 0, "
            "u'4': 0.5}, u'falseNegatives': {u'1': 65, u'3': 39, u'2': 4, u'4': 29}, u'falsePositives': {u'1': 13, u'3': 140, u'4': 37}}, "
            "u'falseNegatives': "
            "137, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 115}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 71, u'iteration': 668607}",
            "{u'name': u'FMetricDev', u'iteration': 395514, u'subtype': u'evaluation', u'epoch': 41, u'values': {u'truePositives': 4361, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9146392617449665, u'precision': 0.9146392617449665, u'f': 0.9146392617449665}, u'macro': {u'recall': "
            "0.46662288671318886, "
            "u'precision': 0.4399642368286857, u'f': 0.45290160627366083}, u'perLabel': {u'truePositives': {u'0': 4077, u'3': 165, u'4': 119}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9738445001791473, u'3': 0.5436573311367381, u'2': 0, u'4': 0.7}, u'recall': {u'1': 0.0, u'0': 0.9864505202032422, "
            "u'3': 0.7268722466960352, u'2': 0.0, u'4': 0.6197916666666666}, u'precision': {u'1': 0, u'0': 0.9615566037735849, "
            "u'3': 0.4342105263157895, "
            "u'2': 0, u'4': 0.8040540540540541}, u'falseNegatives': {u'1': 119, u'0': 56, u'3': 62, u'2': 97, u'4': 73}, u'falsePositives': {u'0': "
            "163, "
            "u'3': 215, u'4': 29}}, u'falseNegatives': 407, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4361}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 30, u'type': u'duration', u'iteration': 291927}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 92, u'type': u'duration', u'iteration': 875781}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 25, u'type': u'duration', u'iteration': 244842}",
            "{u'name': u'AccDev', u'iteration': 113004, u'subtype': u'evaluation', u'epoch': 11, u'values': {u'accumAccuracy': 4186.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8779362416107382}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 819279, u'subtype': u'train', u'epoch': 86, u'values': {u'accumAccuracy': 70999.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9424437512444415}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 58, u'type': u'duration', u'iteration': 555603}",
            "{u'name': u'LossDev', u'iteration': 800445, u'subtype': u'evaluation', u'epoch': 84, u'values': {u'loss': 0.19740791618824005, "
            "u'accumLoss': "
            "941.2409443855286, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 28, u'iteration': 263676}",
            "{u'name': u'AccDev', u'iteration': 263676, u'subtype': u'evaluation', u'epoch': 27, u'values': {u'accumAccuracy': 4288.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8993288590604027}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 51, u'type': u'duration', u'iteration': 489684}",
            u"The unknown symbol of the lexicon 'label_lexicon' wasn't defined.",
            "{u'name': u'CustomMetricDev', u'iteration': 499101, u'subtype': u'evaluation', u'epoch': 52, u'values': {u'truePositives': 101, "
            "u'numExamples': "
            "427, u'micro': {u'recall': 0.554945054945055, u'precision': 0.29190751445086704, u'f': 0.38257575757575757}, u'macro': {u'recall': "
            "0.28535353535353536, u'precision': 0.17374665135859166, u'f': 0.2159843217493627}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 66, "
            "u'2': 0, "
            "u'4': 35}, u'f': {u'1': 0, u'3': 0.35106382978723405, u'2': 0, u'4': 0.48611111111111116}, u'recall': {u'1': 0.0, "
            "u'3': 0.6111111111111112, "
            "u'2': 0.0, u'4': 0.5303030303030303}, u'precision': {u'1': 0, u'3': 0.2462686567164179, u'2': 0, u'4': 0.44871794871794873}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 42, u'2': 4, u'4': 31}, u'falsePositives': {u'3': 202, u'4': 43}}, u'falseNegatives': 81, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 101}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 668607, u'subtype': u'evaluation', u'epoch': 70, u'values': {u'truePositives': 4411, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9251258389261745, u'precision': 0.9251258389261745, u'f': 0.9251258389261745}, u'macro': {u'recall': "
            "0.5234321584888705, "
            "u'precision': 0.6364353286564576, u'f': 0.574428926595962}, u'perLabel': {u'truePositives': {u'1': 6, u'0': 4074, u'3': 178, "
            "u'4': 153}, "
            "u'f': {u'1': 0.09523809523809523, u'0': 0.9763930497303775, u'3': 0.5903814262023217, u'2': 0, u'4': 0.8383561643835618}, "
            "u'recall': {u'1': "
            "0.05042016806722689, u'0': 0.9857246552141302, u'3': 0.7841409691629956, u'2': 0.0, u'4': 0.796875}, u'precision': {u'1': "
            "0.8571428571428571, "
            "u'0': 0.9672364672364673, u'3': 0.4734042553191489, u'2': 0, u'4': 0.884393063583815}, u'falseNegatives': {u'1': 113, u'0': 59, "
            "u'3': 49, "
            "u'2': 97, u'4': 39}, u'falsePositives': {u'1': 1, u'0': 138, u'3': 198, u'4': 20}}, u'falseNegatives': 357, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4411}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 48, u'iteration': 452016}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 79, u'type': u'duration', u'iteration': 753360}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 61, u'type': u'duration', u'iteration': 583854}",
            "{u'name': u'LossDev', u'iteration': 875781, u'subtype': u'evaluation', u'epoch': 92, u'values': {u'loss': 0.19271689653396606, "
            "u'accumLoss': "
            "918.8741626739502, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 38, u'type': u'duration', u'iteration': 367263}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 2, u'type': u'duration', u'iteration': 28251}",
            "{u'learn_rate': [0.001], u'epoch': 79, u'iteration': 743943}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 53, u'type': u'duration', u'iteration': 508518}",
            "{u'name': u'LossDev', u'iteration': 452016, u'subtype': u'evaluation', u'epoch': 47, u'values': {u'loss': 0.2407522201538086, "
            "u'accumLoss': "
            "1147.9065856933594, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 78, u'type': u'duration', u'iteration': 743943}",
            "{u'name': u'FMetricDev', u'iteration': 555603, u'subtype': u'evaluation', u'epoch': 58, u'values': {u'truePositives': 4400, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9228187919463087, u'precision': 0.9228187919463087, u'f': 0.9228187919463087}, u'macro': {u'recall': "
            "0.508300400940036, "
            "u'precision': 0.46206535923030767, u'f': 0.48408139898925756}, u'perLabel': {u'truePositives': {u'0': 4074, u'3': 177, u'4': 149}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9763930497303775, u'3': 0.5756097560975609, u'2': 0, u'4': 0.8277777777777778}, u'recall': {u'1': 0.0, "
            "u'0': 0.9857246552141302, "
            "u'3': 0.7797356828193832, u'2': 0.0, u'4': 0.7760416666666666}, u'precision': {u'1': 0, u'0': 0.9672364672364673, "
            "u'3': 0.45618556701030927, "
            "u'2': 0, u'4': 0.8869047619047619}, u'falseNegatives': {u'1': 119, u'0': 59, u'3': 50, u'2': 97, u'4': 43}, u'falsePositives': {u'0': "
            "138, "
            "u'3': 211, u'4': 19}}, u'falseNegatives': 368, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4400}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 90, u'type': u'duration', u'iteration': 856947}",
            "{u'name': u'AccTrain', u'iteration': 706275, u'subtype': u'train', u'epoch': 74, u'values': {u'accumAccuracy': 70646.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9377580142032256}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 254259, u'subtype': u'train', u'epoch': 26, u'values': {u'accumAccuracy': 68276.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9062985332182917}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 291927, u'subtype': u'train', u'epoch': 30, u'values': {u'accumAccuracy': 68761.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9127364438839849}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 282510, u'subtype': u'train', u'epoch': 29, u'values': {u'loss': 0.25774638736043837, "
            "u'accumLoss': "
            "19417.324091798626, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 72, u'type': u'duration', u'iteration': 687441}",
            "{u'name': u'AccDev', u'iteration': 178923, u'subtype': u'evaluation', u'epoch': 18, u'values': {u'accumAccuracy': 4220.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8850671140939598}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 838113, u'subtype': u'train', u'epoch': 88, u'values': {u'loss': 0.15391528503434945, "
            "u'accumLoss': "
            "11595.207998062717, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 866364, u'subtype': u'train', u'epoch': 91, u'values': {u'accumAccuracy': 71131.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9441959248689188}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 73, u'iteration': 687441}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 88, u'type': u'duration', u'iteration': 838113}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 75, u'type': u'duration', u'iteration': 715692}",
            "{u'name': u'AccDev', u'iteration': 452016, u'subtype': u'evaluation', u'epoch': 47, u'values': {u'accumAccuracy': 4374.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9173657718120806}, u'type': u'metric'}",
            u'Training algorithm: Adagrad', "{u'learn_rate': [0.001], u'epoch': 81, u'iteration': 762777}",
            "{u'name': u'AccDev', u'iteration': 621522, u'subtype': u'evaluation', u'epoch': 65, u'values': {u'accumAccuracy': 4408.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.924496644295302}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 131838, u'subtype': u'evaluation', u'epoch': 13, u'values': {u'truePositives': 4198, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8804530201342282, u'precision': 0.8804530201342282, u'f': 0.8804530201342282}, u'macro': {u'recall': "
            "0.2915355976430229, "
            "u'precision': 0.48427095948292953, u'f': 0.36396243959844493}, u'perLabel': {u'truePositives': {u'1': 1, u'0': 4093, u'3': 103, "
            "u'4': 1}, "
            "u'f': {u'1': 0.016129032258064516, u'0': 0.9580992509363296, u'3': 0.35640138408304495, u'2': 0, u'4': 0.010362694300518135}, "
            "u'recall': {u'1': "
            "0.008403361344537815, u'0': 0.990321800145173, u'3': 0.45374449339207046, u'2': 0.0, u'4': 0.005208333333333333}, u'precision': {u'1': "
            "0.2, "
            "u'0': 0.9279075039673543, u'3': 0.2934472934472934, u'2': 0, u'4': 1.0}, u'falseNegatives': {u'1': 118, u'0': 40, u'3': 124, u'2': 97, "
            "u'4': 191}, "
            "u'falsePositives': {u'1': 4, u'0': 318, u'3': 248}}, u'falseNegatives': 570, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4198}, "
            "u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 197757, u'subtype': u'evaluation', u'epoch': 20, u'values': {u'truePositives': 4228, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.886744966442953, u'precision': 0.886744966442953, u'f': 0.886744966442953}, u'macro': {u'recall': "
            "0.321432402890243, "
            "u'precision': 0.4232429422938364, u'f': 0.3653780048652343}, u'perLabel': {u'truePositives': {u'0': 4090, u'3': 126, u'4': 12}, "
            "u'f': {u'1': 0, "
            "u'0': 0.96291936433196, u'3': 0.407108239095315, u'2': 0, u'4': 0.11650485436893204}, u'recall': {u'1': 0.0, u'0': 0.9895959351560609, "
            "u'3': 0.5550660792951542, u'2': 0.0, u'4': 0.0625}, u'precision': {u'1': 0, u'0': 0.9376432828977533, u'3': 0.32142857142857145, "
            "u'2': 0, "
            "u'4': 0.8571428571428571}, u'falseNegatives': {u'1': 119, u'0': 43, u'3': 101, u'2': 97, u'4': 180}, u'falsePositives': {u'0': 272, "
            "u'3': 266, "
            "u'4': 2}}, u'falseNegatives': 540, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4228}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 743943, u'subtype': u'evaluation', u'epoch': 78, u'values': {u'truePositives': 117, "
            "u'numExamples': "
            "451, u'micro': {u'recall': 0.4642857142857143, u'precision': 0.370253164556962, u'f': 0.4119718309859155}, u'macro': {u'recall': "
            "0.33572777322777325, u'precision': 0.30681863477827603, u'f': 0.320622870987791}, u'perLabel': {u'truePositives': {u'1': 7, u'3': 71, "
            "u'2': 0, "
            "u'4': 39}, u'f': {u'1': 0.15217391304347827, u'3': 0.42900302114803623, u'2': 0, u'4': 0.5531914893617023}, u'recall': {u'1': "
            "0.0945945945945946, "
            "u'3': 0.6574074074074074, u'2': 0.0, u'4': 0.5909090909090909}, u'precision': {u'1': 0.3888888888888889, u'3': 0.3183856502242152, "
            "u'2': 0, "
            "u'4': 0.52}, u'falseNegatives': {u'1': 67, u'3': 37, u'2': 4, u'4': 27}, u'falsePositives': {u'1': 11, u'3': 152, u'4': 36}}, "
            "u'falseNegatives': "
            "135, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 117}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 583854, u'subtype': u'evaluation', u'epoch': 61, u'values': {u'loss': 0.2176213562488556, "
            "u'accumLoss': "
            "1037.6186265945435, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 357846, u'subtype': u'train', u'epoch': 37, u'values': {u'accumAccuracy': 69350.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9205548549810845}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 414348, u'subtype': u'evaluation', u'epoch': 43, u'values': {u'loss': 0.24926747381687164, "
            "u'accumLoss': "
            "1188.507315158844, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 546186, u'subtype': u'train', u'epoch': 57, u'values': {u'accumAccuracy': 70182.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9315988584323356}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 904032, u'subtype': u'evaluation', u'epoch': 95, u'values': {u'accumAccuracy': 4448.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9328859060402684}, u'type': u'metric'}",
            "{u'duration': 14, u'subtype': u'training', u'epoch': 5, u'type': u'duration', u'iteration': 56502}",
            "{u'name': u'AccDev', u'iteration': 508518, u'subtype': u'evaluation', u'epoch': 53, u'values': {u'accumAccuracy': 4389.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.920511744966443}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 856947, u'subtype': u'evaluation', u'epoch': 90, u'values': {u'truePositives': 133, "
            "u'numExamples': "
            "431, u'micro': {u'recall': 0.5277777777777778, u'precision': 0.42628205128205127, u'f': 0.4716312056737589}, u'macro': {u'recall': "
            "0.38953726453726456, u'precision': 0.3478516077837174, u'f': 0.3675161610032425}, u'perLabel': {u'truePositives': {u'1': 20, u'3': 72, "
            "u'2': 0, "
            "u'4': 41}, u'f': {u'1': 0.34782608695652173, u'3': 0.47682119205298024, u'2': 0, u'4': 0.5734265734265734}, u'recall': {u'1': "
            "0.2702702702702703, "
            "u'3': 0.6666666666666666, u'2': 0.0, u'4': 0.6212121212121212}, u'precision': {u'1': 0.4878048780487805, u'3': 0.3711340206185567, "
            "u'2': 0, "
            "u'4': 0.5324675324675324}, u'falseNegatives': {u'1': 54, u'3': 36, u'2': 4, u'4': 25}, u'falsePositives': {u'1': 21, u'3': 122, "
            "u'4': 36}}, "
            "u'falseNegatives': 119, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 133}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 706275, u'subtype': u'evaluation', u'epoch': 74, u'values': {u'loss': 0.20472489297389984, "
            "u'accumLoss': "
            "976.1282896995544, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 687441, u'subtype': u'evaluation', u'epoch': 72, u'values': {u'loss': 0.20576699078083038, "
            "u'accumLoss': "
            "981.0970120429993, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 122421, u'subtype': u'train', u'epoch': 12, u'values': {u'loss': 0.32361252781844607, "
            "u'accumLoss': "
            "24379.349783202633, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 404931, u'subtype': u'train', u'epoch': 42, u'values': {u'loss': 0.22188150123609604, "
            "u'accumLoss': "
            "16715.442895621294, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 75336, u'subtype': u'train', u'epoch': 7, u'values': {u'loss': 0.3760271395917055, u'accumLoss': "
            "28328.004561141133, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 28, u'type': u'duration', u'iteration': 273093}",
            "{u'learn_rate': [0.001], u'epoch': 89, u'iteration': 838113}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 18, u'type': u'duration', u'iteration': 178923}",
            "{u'name': u'LossTrain', u'iteration': 470850, u'subtype': u'train', u'epoch': 49, u'values': {u'loss': 0.20543410790643418, "
            "u'accumLoss': "
            "15476.37851913122, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 37668, u'subtype': u'train', u'epoch': 3, u'values': {u'loss': 0.47130843900950625, u'accumLoss': "
            "35506.02125278115, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 169506, u'subtype': u'evaluation', u'epoch': 17, u'values': {u'truePositives': 4211, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8831795302013423, u'precision': 0.8831795302013423, u'f': 0.8831795302013423}, u'macro': {u'recall': "
            "0.2968428914439242, "
            "u'precision': 0.44626490628963167, u'f': 0.3565312207380818}, u'perLabel': {u'truePositives': {u'0': 4100, u'3': 107, u'4': 4}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9599625380472956, u'3': 0.36769759450171824, u'2': 0, u'4': 0.04081632653061225}, u'recall': {u'1': 0.0, "
            "u'0': 0.9920154851197677, "
            "u'3': 0.4713656387665198, u'2': 0.0, u'4': 0.020833333333333332}, u'precision': {u'1': 0, u'0': 0.9299160807439328, "
            "u'3': 0.30140845070422534, "
            "u'2': 0, u'4': 1.0}, u'falseNegatives': {u'1': 119, u'0': 33, u'3': 120, u'2': 97, u'4': 188}, u'falsePositives': {u'0': 309, "
            "u'3': 248}}, "
            "u'falseNegatives': 557, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4211}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 70, u'type': u'duration', u'iteration': 668607}",
            "{u'name': u'LossTrain', u'iteration': 819279, u'subtype': u'train', u'epoch': 86, u'values': {u'loss': 0.1555002187108976, "
            "u'accumLoss': "
            "11714.60897658547, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 904032, u'subtype': u'train', u'epoch': 95, u'values': {u'loss': 0.1486481143937794, "
            "u'accumLoss': "
            "11198.40569785537, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 932283, u'subtype': u'evaluation', u'epoch': 98, u'values': {u'loss': 0.1898699700832367, "
            "u'accumLoss': "
            "905.3000173568726, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 329595, u'subtype': u'evaluation', u'epoch': 34, u'values': {u'loss': 0.2717955410480499, "
            "u'accumLoss': "
            "1295.921139717102, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 113004, u'subtype': u'train', u'epoch': 11, u'values': {u'accumAccuracy': 66534.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.8831751509922346}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 64, u'type': u'duration', u'iteration': 612105}",
            "{u'name': u'AccTrain', u'iteration': 922866, u'subtype': u'train', u'epoch': 97, u'values': {u'accumAccuracy': 71270.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9460410167916639}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 226008, u'subtype': u'evaluation', u'epoch': 23, u'values': {u'truePositives': 44, "
            "u'numExamples': "
            "441, u'micro': {u'recall': 0.24175824175824176, u'precision': 0.14521452145214522, u'f': 0.18144329896907216}, u'macro': {u'recall': "
            "0.10185185185185185, u'precision': 0.03985507246376811, u'f': 0.057291666666666664}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 44, u'2': 0, "
            "u'4': 0}, u'f': {u'1': 0, u'3': 0.22916666666666666, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.4074074074074074, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0.15942028985507245, u'2': 0, u'4': 0.0}, u'falseNegatives': {u'1': 4, u'3': 64, u'2': 4, u'4': 66}, "
            "u'falsePositives': {u'3': 232, u'4': 27}}, u'falseNegatives': 138, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 44}, "
            "u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 442599, u'subtype': u'evaluation', u'epoch': 46, u'values': {u'loss': 0.24321921169757843, "
            "u'accumLoss': "
            "1159.669201374054, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 84753, u'subtype': u'evaluation', u'epoch': 8, u'values': {u'accumAccuracy': 4169.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8743708053691275}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 32, u'type': u'duration', u'iteration': 310761}", u'floatX=float32',
            "{u'name': u'LossTrain', u'iteration': 273093, u'subtype': u'train', u'epoch': 28, u'values': {u'loss': 0.26066360391461074, "
            "u'accumLoss': "
            "19637.0926009072, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 800445, u'subtype': u'evaluation', u'epoch': 84, u'values': {u'truePositives': 122, "
            "u'numExamples': "
            "435, u'micro': {u'recall': 0.48412698412698413, u'precision': 0.4, u'f': 0.4380610412926392}, u'macro': {u'recall': 0.3547467922467923, "
            "u'precision': 0.33291666666666664, u'f': 0.3434852268349404}, u'perLabel': {u'truePositives': {u'1': 14, u'3': 69, u'2': 0, u'4': 39}, "
            "u'f': {u'1': 0.2692307692307693, u'3': 0.448051948051948, u'2': 0, u'4': 0.5531914893617023}, u'recall': {u'1': 0.1891891891891892, "
            "u'3': 0.6388888888888888, u'2': 0.0, u'4': 0.5909090909090909}, u'precision': {u'1': 0.4666666666666667, u'3': 0.345, u'2': 0, "
            "u'4': 0.52}, "
            "u'falseNegatives': {u'1': 60, u'3': 39, u'2': 4, u'4': 27}, u'falsePositives': {u'1': 16, u'3': 131, u'4': 36}}, u'falseNegatives': "
            "130, "
            "u'beta': 1.0, u'numLabels': 4, u'falsePositives': 122}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 301344, u'subtype': u'evaluation', u'epoch': 31, u'values': {u'loss': 0.27880197763442993, "
            "u'accumLoss': "
            "1329.327829360962, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 932283, u'subtype': u'evaluation', u'epoch': 98, u'values': {u'truePositives': 141, "
            "u'numExamples': "
            "478, u'micro': {u'recall': 0.46229508196721314, u'precision': 0.44904458598726116, u'f': 0.4555735056542811}, u'macro': {u'recall': "
            "0.42124870085396404, u'precision': 0.5204190266634316, u'f': 0.4656118766215342}, u'perLabel': {u'truePositives': {u'1': 26, u'3': 71, "
            "u'2': 4, "
            "u'4': 40}, u'f': {u'1': 0.41600000000000004, u'3': 0.49650349650349657, u'2': 0.12698412698412698, u'4': 0.5517241379310346}, "
            "u'recall': {u'1': "
            "0.35135135135135137, u'3': 0.6574074074074074, u'2': 0.07017543859649122, u'4': 0.6060606060606061}, u'precision': {u'1': "
            "0.5098039215686274, "
            "u'3': 0.398876404494382, u'2': 0.6666666666666666, u'4': 0.5063291139240507}, u'falseNegatives': {u'1': 48, u'3': 37, u'2': 53, "
            "u'4': 26}, "
            "u'falsePositives': {u'1': 25, u'3': 107, u'2': 2, u'4': 39}}, u'falseNegatives': 164, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 141}, "
            "u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 21, u'iteration': 197757}",
            "{u'duration': 12, u'subtype': u'training', u'epoch': 11, u'type': u'duration', u'iteration': 113004}",
            "{u'name': u'AccTrain', u'iteration': 612105, u'subtype': u'train', u'epoch': 64, u'values': {u'accumAccuracy': 70362.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9339881861020773}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 404931, u'subtype': u'evaluation', u'epoch': 42, u'values': {u'truePositives': 88, "
            "u'numExamples': "
            "452, u'micro': {u'recall': 0.4835164835164835, u'precision': 0.24581005586592178, u'f': 0.3259259259259259}, u'macro': {u'recall': "
            "0.24494949494949497, u'precision': 0.13654240766073872, u'f': 0.17534313869753312}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 60, u'2': 0, "
            "u'4': 28}, u'f': {u'1': 0, u'3': 0.31578947368421056, u'2': 0, u'4': 0.368421052631579}, u'recall': {u'1': 0.0, "
            "u'3': 0.5555555555555556, "
            "u'2': 0.0, u'4': 0.42424242424242425}, u'precision': {u'1': 0, u'3': 0.22058823529411764, u'2': 0, u'4': 0.32558139534883723}, "
            "u'falseNegatives': "
            "{u'1': 4, u'3': 48, u'2': 4, u'4': 38}, u'falsePositives': {u'3': 212, u'4': 58}}, u'falseNegatives': 94, u'beta': 1.0, u'numLabels': "
            "4, "
            "u'falsePositives': 88}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 80, u'iteration': 753360}",
            "{u'name': u'AccTrain', u'iteration': 414348, u'subtype': u'train', u'epoch': 43, u'values': {u'accumAccuracy': 69604.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9239264618039424}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 348429, u'subtype': u'evaluation', u'epoch': 36, u'values': {u'loss': 0.26613062620162964, "
            "u'accumLoss': "
            "1268.9108257293701, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 18834, u'subtype': u'evaluation', u'epoch': 1, u'values': {u'truePositives': 4133, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8668204697986577, u'precision': 0.8668204697986577, u'f': 0.8668204697986577}, u'macro': {u'recall': 0.2, "
            "u'precision': "
            "0.17336409395973154, u'f': 0.18573194023143466}, u'perLabel': {u'truePositives': {u'0': 4133}, u'f': {u'1': 0, "
            "u'0': 0.9286597011571733, u'3': 0, "
            "u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'0': 1.0, u'3': 0.0, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0, "
            "u'0': 0.8668204697986577, u'3': 0, "
            "u'2': 0, u'4': 0}, u'falseNegatives': {u'1': 119, u'3': 227, u'2': 97, u'4': 192}, u'falsePositives': {u'0': 635}}, u'falseNegatives': "
            "635, "
            "u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4133}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 461433, u'subtype': u'evaluation', u'epoch': 48, u'values': {u'truePositives': 95, "
            "u'numExamples': "
            "425, u'micro': {u'recall': 0.521978021978022, u'precision': 0.28106508875739644, u'f': 0.36538461538461536}, u'macro': {u'recall': "
            "0.2670454545454546, u'precision': 0.1642409314823108, u'f': 0.20339058047540107}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 63, "
            "u'2': 0, "
            "u'4': 32}, u'f': {u'1': 0, u'3': 0.34146341463414637, u'2': 0, u'4': 0.44755244755244755}, u'recall': {u'1': 0.0, "
            "u'3': 0.5833333333333334, "
            "u'2': 0.0, u'4': 0.48484848484848486}, u'precision': {u'1': 0, u'3': 0.2413793103448276, u'2': 0, u'4': 0.4155844155844156}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 45, u'2': 4, u'4': 34}, u'falsePositives': {u'3': 198, u'4': 45}}, u'falseNegatives': 87, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 95}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 941700, u'subtype': u'evaluation', u'epoch': 99, u'values': {u'truePositives': 4456, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9345637583892618, u'precision': 0.9345637583892618, u'f': 0.9345637583892618}, u'macro': {u'recall': "
            "0.5961429593195391, "
            "u'precision': 0.7671728704163602, u'f': 0.670929941990435}, u'perLabel': {u'truePositives': {u'1': 35, u'0': 4072, u'3': 183, u'2': 6, "
            "u'4': 160}, "
            "u'f': {u'1': 0.4142011834319526, u'0': 0.9775537150402112, u'3': 0.6642468239564429, u'2': 0.1142857142857143, "
            "u'4': 0.8421052631578947}, "
            "u'recall': {u'1': 0.29411764705882354, u'0': 0.9852407452213888, u'3': 0.8061674008810573, u'2': 0.061855670103092786, "
            "u'4': 0.8333333333333334}, "
            "u'precision': {u'1': 0.7, u'0': 0.9699857074797522, u'3': 0.5648148148148148, u'2': 0.75, u'4': 0.851063829787234}, u'falseNegatives': "
            "{u'1': 84, "
            "u'0': 61, u'3': 44, u'2': 91, u'4': 32}, u'falsePositives': {u'1': 15, u'0': 126, u'3': 141, u'2': 2, u'4': 28}}, u'falseNegatives': "
            "312, "
            "u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4456}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 715692, u'subtype': u'evaluation', u'epoch': 75, u'values': {u'loss': 0.2033444046974182, "
            "u'accumLoss': "
            "969.54612159729, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 67, u'type': u'duration', u'iteration': 640356}",
            "{u'name': u'LossTrain', u'iteration': 753360, u'subtype': u'train', u'epoch': 79, u'values': {u'loss': 0.1617093423609975, "
            "u'accumLoss': "
            "12182.373306765745, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 809862, u'subtype': u'evaluation', u'epoch': 85, u'values': {u'truePositives': 4430, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9291107382550335, u'precision': 0.9291107382550335, u'f': 0.9291107382550335}, u'macro': {u'recall': "
            "0.5593461132055922, "
            "u'precision': 0.5955492528855189, u'f': 0.5768802431885925}, u'perLabel': {u'truePositives': {u'1': 19, u'0': 4065, u'3': 185, "
            "u'4': 161}, "
            "u'f': {u'1': 0.25675675675675674, u'0': 0.9779862865391555, u'3': 0.6218487394957982, u'2': 0, u'4': 0.8429319371727747}, "
            "u'recall': {u'1': "
            "0.15966386554621848, u'0': 0.9835470602467941, u'3': 0.8149779735682819, u'2': 0.0, u'4': 0.8385416666666666}, u'precision': {u'1': "
            "0.6551724137931034, u'0': 0.972488038277512, u'3': 0.5027173913043478, u'2': 0.0, u'4': 0.8473684210526315}, u'falseNegatives': {u'1': "
            "100, "
            "u'0': 68, u'3': 42, u'2': 97, u'4': 31}, u'falsePositives': {u'1': 10, u'0': 115, u'3': 183, u'2': 1, u'4': 29}}, u'falseNegatives': "
            "338, "
            "u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4430}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 61, u'type': u'duration', u'iteration': 583854}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 66, u'type': u'duration', u'iteration': 630939}",
            "{u'name': u'CustomMetricDev', u'iteration': 725109, u'subtype': u'evaluation', u'epoch': 76, u'values': {u'truePositives': 116, "
            "u'numExamples': "
            "449, u'micro': {u'recall': 0.4603174603174603, u'precision': 0.3706070287539936, u'f': 0.4106194690265486}, u'macro': {u'recall': "
            "0.33046683046683045, u'precision': 0.33, u'f': 0.3302332502511067}, u'perLabel': {u'truePositives': {u'1': 7, u'3': 72, u'2': 0, "
            "u'4': 37}, "
            "u'f': {u'1': 0.1590909090909091, u'3': 0.43243243243243246, u'2': 0, u'4': 0.5285714285714286}, u'recall': {u'1': 0.0945945945945946, "
            "u'3': 0.6666666666666666, u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 0.5, u'3': 0.32, u'2': 0, u'4': 0.5}, "
            "u'falseNegatives': {"
            "u'1': 67, u'3': 36, u'2': 4, u'4': 29}, u'falsePositives': {u'1': 7, u'3': 153, u'4': 37}}, u'falseNegatives': 136, u'beta': 1.0, "
            "u'numLabels': 4, "
            "u'falsePositives': 116}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 64, u'iteration': 602688}",
            "{u'name': u'LossDev', u'iteration': 320178, u'subtype': u'evaluation', u'epoch': 33, u'values': {u'loss': 0.2749601900577545, "
            "u'accumLoss': "
            "1311.0101861953735, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 39, u'type': u'duration', u'iteration': 376680}",
            "{u'name': u'AccDev', u'iteration': 282510, u'subtype': u'evaluation', u'epoch': 29, u'values': {u'accumAccuracy': 4308.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9035234899328859}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 452016, u'subtype': u'train', u'epoch': 47, u'values': {u'loss': 0.2098515367076344, "
            "u'accumLoss': "
            "15809.165517869638, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 13, u'subtype': u'training', u'epoch': 4, u'type': u'duration', u'iteration': 47085}",
            "{u'name': u'CustomMetricDev', u'iteration': 18834, u'subtype': u'evaluation', u'epoch': 1, u'values': {u'truePositives': 0, "
            "u'numExamples': 16, "
            "u'micro': {u'recall': 0.0, u'precision': 0, u'f': 0}, u'macro': {u'recall': 0.0, u'precision': 0.0, u'f': 0}, u'perLabel': {"
            "u'truePositives': {"
            "u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'f': {u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.0, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'falseNegatives': {u'1': 4, u'3': 4, u'2': 4, u'4': 4}, u'falsePositives': {}}, "
            "u'falseNegatives': 16, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 0}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 291927, u'subtype': u'train', u'epoch': 30, u'values': {u'loss': 0.2548729231500087, "
            "u'accumLoss': "
            "19200.851665505907, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 856947, u'subtype': u'evaluation', u'epoch': 90, u'values': {u'truePositives': 4441, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9314177852348994, u'precision': 0.9314177852348994, u'f': 0.9314177852348994}, u'macro': {u'recall': "
            "0.569639050546145, "
            "u'precision': 0.5972070847205038, u'f': 0.5830974049408457}, u'perLabel': {u'truePositives': {u'1': 26, u'0': 4071, u'3': 183, "
            "u'4': 161}, "
            "u'f': {u'1': 0.32499999999999996, u'0': 0.978018018018018, u'3': 0.6387434554973822, u'2': 0, u'4': 0.8451443569553806}, "
            "u'recall': {u'1': "
            "0.2184873949579832, u'0': 0.9849987902250181, u'3': 0.8061674008810573, u'2': 0.0, u'4': 0.8385416666666666}, u'precision': {u'1': "
            "0.6341463414634146, u'0': 0.9711354961832062, u'3': 0.5289017341040463, u'2': 0, u'4': 0.8518518518518519}, u'falseNegatives': {u'1': "
            "93, "
            "u'0': 62, u'3': 44, u'2': 97, u'4': 31}, u'falsePositives': {u'1': 15, u'0': 121, u'3': 163, u'4': 28}}, u'falseNegatives': 327, "
            "u'beta': 1.0, "
            "u'numLabels': 5, u'falsePositives': 4441}, u'type': u'metric'}",
            "{u'duration': 6, u'subtype': u'training', u'epoch': 14, u'type': u'duration', u'iteration': 141255}",
            "{u'name': u'AccDev', u'iteration': 160089, u'subtype': u'evaluation', u'epoch': 16, u'values': {u'accumAccuracy': 4204.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8817114093959731}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 24, u'type': u'duration', u'iteration': 235425}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 47, u'type': u'duration', u'iteration': 452016}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 56, u'type': u'duration', u'iteration': 536769}",
            "{u'name': u'LossTrain', u'iteration': 781611, u'subtype': u'train', u'epoch': 82, u'values': {u'loss': 0.1589076074563964, "
            "u'accumLoss': "
            "11971.304607727623, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 9417, u'subtype': u'evaluation', u'epoch': 0, u'values': {u'truePositives': 0, "
            "u'numExamples': 16, "
            "u'micro': {u'recall': 0.0, u'precision': 0, u'f': 0}, u'macro': {u'recall': 0.0, u'precision': 0.0, u'f': 0}, u'perLabel': {"
            "u'truePositives': {"
            "u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'f': {u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'3': 0.0, u'2': 0.0, "
            "u'4': 0.0}, "
            "u'precision': {u'1': 0, u'3': 0, u'2': 0, u'4': 0}, u'falseNegatives': {u'1': 4, u'3': 4, u'2': 4, u'4': 4}, u'falsePositives': {}}, "
            "u'falseNegatives': 16, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 0}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 621522, u'subtype': u'evaluation', u'epoch': 65, u'values': {u'loss': 0.21278329193592072, "
            "u'accumLoss': "
            "1014.55073595047, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 41, u'iteration': 386097}",
            "{u'name': u'AccDev', u'iteration': 94170, u'subtype': u'evaluation', u'epoch': 9, u'values': {u'accumAccuracy': 4176.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.8758389261744967}, u'type': u'metric'}",
            u'Number of examples: 4768', "{u'learn_rate': [0.001], u'epoch': 20, u'iteration': 188340}",
            "{u'learn_rate': [0.001], u'epoch': 92, u'iteration': 866364}",
            "{u'name': u'AccDev', u'iteration': 838113, u'subtype': u'evaluation', u'epoch': 88, u'values': {u'accumAccuracy': 4446.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9324664429530202}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 772194, u'subtype': u'evaluation', u'epoch': 81, u'values': {u'loss': 0.1989148110151291, "
            "u'accumLoss': "
            "948.4258189201355, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 35, u'type': u'duration', u'iteration': 339012}",
            "{u'name': u'FMetricDev', u'iteration': 649773, u'subtype': u'evaluation', u'epoch': 68, u'values': {u'truePositives': 4404, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9236577181208053, u'precision': 0.9236577181208053, u'f': 0.9236577181208053}, u'macro': {u'recall': "
            "0.5181965776850512, "
            "u'precision': 0.6113405825286801, u'f': 0.5609281550443258}, u'perLabel': {u'truePositives': {u'1': 3, u'0': 4070, u'3': 178, "
            "u'4': 153}, "
            "u'f': {u'1': 0.04878048780487805, u'0': 0.9761362273653915, u'3': 0.5836065573770493, u'2': 0, u'4': 0.8337874659400546}, "
            "u'recall': {u'1': "
            "0.025210084033613446, u'0': 0.9847568352286474, u'3': 0.7841409691629956, u'2': 0.0, u'4': 0.796875}, u'precision': {u'1': 0.75, "
            "u'0': 0.9676652401331431, u'3': 0.46475195822454307, u'2': 0, u'4': 0.8742857142857143}, u'falseNegatives': {u'1': 116, u'0': 63, "
            "u'3': 49, "
            "u'2': 97, u'4': 39}, u'falsePositives': {u'1': 1, u'0': 136, u'3': 205, u'4': 22}}, u'falseNegatives': 364, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4404}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 734526, u'subtype': u'evaluation', u'epoch': 77, u'values': {u'truePositives': 4423, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9276426174496645, u'precision': 0.9276426174496645, u'f': 0.9276426174496645}, u'macro': {u'recall': "
            "0.5334887512916082, "
            "u'precision': 0.5968409154083577, u'f': 0.5633894678011014}, u'perLabel': {u'truePositives': {u'1': 11, u'0': 4080, u'3': 176, "
            "u'4': 156}, "
            "u'f': {u'1': 0.16176470588235295, u'0': 0.9770114942528736, u'3': 0.6068965517241379, u'2': 0, u'4': 0.8409703504043127}, "
            "u'recall': {u'1': "
            "0.09243697478991597, u'0': 0.9871763851923542, u'3': 0.775330396475771, u'2': 0.0, u'4': 0.8125}, u'precision': {u'1': "
            "0.6470588235294118, "
            "u'0': 0.9670538042190092, u'3': 0.4985835694050991, u'2': 0, u'4': 0.8715083798882681}, u'falseNegatives': {u'1': 108, u'0': 53, "
            "u'3': 51, "
            "u'2': 97, u'4': 36}, u'falsePositives': {u'1': 6, u'0': 139, u'3': 177, u'4': 23}}, u'falseNegatives': 345, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4423}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 706275, u'subtype': u'evaluation', u'epoch': 74, u'values': {u'truePositives': 116, "
            "u'numExamples': "
            "451, u'micro': {u'recall': 0.4603174603174603, u'precision': 0.3682539682539683, u'f': 0.40917107583774254}, u'macro': {u'recall': "
            "0.33046683046683045, u'precision': 0.32929515418502203, u'f': 0.3298799519315558}, u'perLabel': {u'truePositives': {u'1': 7, u'3': 72, "
            "u'2': 0, "
            "u'4': 37}, u'f': {u'1': 0.1590909090909091, u'3': 0.4298507462686567, u'2': 0, u'4': 0.5285714285714286}, u'recall': {u'1': "
            "0.0945945945945946, "
            "u'3': 0.6666666666666666, u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 0.5, u'3': 0.31718061674008813, u'2': 0, "
            "u'4': 0.5}, "
            "u'falseNegatives': {u'1': 67, u'3': 36, u'2': 4, u'4': 29}, u'falsePositives': {u'1': 7, u'3': 155, u'4': 37}}, u'falseNegatives': 136, "
            "u'beta': 1.0, u'numLabels': 4, u'falsePositives': 116}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 640356, u'subtype': u'evaluation', u'epoch': 67, u'values': {u'truePositives': 4408, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.924496644295302, u'precision': 0.924496644295302, u'f': 0.924496644295302}, u'macro': {u'recall': "
            "0.5130729252695694, "
            "u'precision': 0.6127845358761104, u'f': 0.558513249202919}, u'perLabel': {u'truePositives': {u'1': 3, u'0': 4080, u'3': 174, "
            "u'4': 151}, "
            "u'f': {u'1': 0.04878048780487805, u'0': 0.9763101220387653, u'3': 0.5868465430016863, u'2': 0, u'4': 0.8273972602739728}, "
            "u'recall': {u'1': "
            "0.025210084033613446, u'0': 0.9871763851923542, u'3': 0.7665198237885462, u'2': 0.0, u'4': 0.7864583333333334}, u'precision': {u'1': "
            "0.75, "
            "u'0': 0.9656804733727811, u'3': 0.47540983606557374, u'2': 0, u'4': 0.8728323699421965}, u'falseNegatives': {u'1': 116, u'0': 53, "
            "u'3': 53, "
            "u'2': 97, u'4': 41}, u'falsePositives': {u'1': 1, u'0': 145, u'3': 192, u'4': 22}}, u'falseNegatives': 360, u'beta': 1.0, "
            "u'numLabels': 5, "
            "u'falsePositives': 4408}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 150672, u'subtype': u'evaluation', u'epoch': 15, u'values': {u'truePositives': 4199, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8806627516778524, u'precision': 0.8806627516778524, u'f': 0.8806627516778524}, u'macro': {u'recall': "
            "0.29244970618100863, "
            "u'precision': 0.44376566757493185, u'f': 0.352557536073759}, u'perLabel': {u'truePositives': {u'0': 4092, u'3': 106, u'4': 1}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9590999648423767, u'3': 0.3569023569023569, u'2': 0, u'4': 0.010362694300518135}, u'recall': {u'1': 0.0, "
            "u'0': 0.9900798451488023, "
            "u'3': 0.4669603524229075, u'2': 0.0, u'4': 0.005208333333333333}, u'precision': {u'1': 0, u'0': 0.93, u'3': 0.2888283378746594, "
            "u'2': 0, "
            "u'4': 1.0}, u'falseNegatives': {u'1': 119, u'0': 41, u'3': 121, u'2': 97, u'4': 191}, u'falsePositives': {u'0': 308, u'3': 261}}, "
            "u'falseNegatives': 569, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4199}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 894615, u'subtype': u'train', u'epoch': 94, u'values': {u'accumAccuracy': 71185.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9449127231698414}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 85, u'type': u'duration', u'iteration': 809862}",
            "{u'name': u'AccTrain', u'iteration': 734526, u'subtype': u'train', u'epoch': 77, u'values': {u'accumAccuracy': 70750.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9391385146346319}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 386097, u'subtype': u'evaluation', u'epoch': 40, u'values': {u'truePositives': 4355, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9133808724832215, u'precision': 0.9133808724832215, u'f': 0.9133808724832215}, u'macro': {u'recall': "
            "0.45502605102088306, "
            "u'precision': 0.4400561539519968, u'f': 0.44741591967249944}, u'perLabel': {u'truePositives': {u'0': 4084, u'3': 155, u'4': 116}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9724967258006906, u'3': 0.5290102389078498, u'2': 0, u'4': 0.6925373134328358}, u'recall': {u'1': 0.0, u'0': 0.988144205177837, "
            "u'3': 0.6828193832599119, u'2': 0.0, u'4': 0.6041666666666666}, u'precision': {u'1': 0, u'0': 0.9573370839193625, "
            "u'3': 0.43175487465181056, "
            "u'2': 0, u'4': 0.8111888111888111}, u'falseNegatives': {u'1': 119, u'0': 49, u'3': 72, u'2': 97, u'4': 76}, u'falsePositives': {u'0': "
            "182, "
            "u'3': 204, u'4': 27}}, u'falseNegatives': 413, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4355}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 489684, u'subtype': u'train', u'epoch': 51, u'values': {u'loss': 0.20128295767173124, "
            "u'accumLoss': "
            "15163.651616199873, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 329595, u'subtype': u'evaluation', u'epoch': 34, u'values': {u'truePositives': 4343, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9108640939597316, u'precision': 0.9108640939597316, u'f': 0.9108640939597316}, u'macro': {u'recall': "
            "0.44435199295772393, "
            "u'precision': 0.4378104624081006, u'f': 0.4410569738611409}, u'perLabel': {u'truePositives': {u'0': 4082, u'3': 156, u'4': 105}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9720204786284081, u'3': 0.52, u'2': 0, u'4': 0.6542056074766355}, u'recall': {u'1': 0.0, u'0': 0.9876602951850956, "
            "u'3': 0.6872246696035242, u'2': 0.0, u'4': 0.546875}, u'precision': {u'1': 0, u'0': 0.956868260665729, u'3': 0.41823056300268097, "
            "u'2': 0, "
            "u'4': 0.813953488372093}, u'falseNegatives': {u'1': 119, u'0': 51, u'3': 71, u'2': 97, u'4': 87}, u'falsePositives': {u'0': 184, "
            "u'3': 217, "
            "u'4': 24}}, u'falseNegatives': 425, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4343}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 743943, u'subtype': u'train', u'epoch': 78, u'values': {u'accumAccuracy': 70785.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9396031061259706}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 866364, u'subtype': u'evaluation', u'epoch': 91, u'values': {u'accumAccuracy': 4442.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9316275167785235}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 69, u'type': u'duration', u'iteration': 659190}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 52, u'type': u'duration', u'iteration': 499101}",
            "{u'name': u'FMetricDev', u'iteration': 216591, u'subtype': u'evaluation', u'epoch': 22, u'values': {u'truePositives': 4248, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8909395973154363, u'precision': 0.8909395973154363, u'f': 0.8909395973154363}, u'macro': {u'recall': "
            "0.33383770269060353, "
            "u'precision': 0.43813458030614305, u'f': 0.3789406562394183}, u'perLabel': {u'truePositives': {u'0': 4098, u'3': 129, u'4': 21}, "
            "u'f': {u'1': 0, "
            "u'0': 0.96457573261151, u'3': 0.42434210526315785, u'2': 0, u'4': 0.19534883720930232}, u'recall': {u'1': 0.0, "
            "u'0': 0.9915315751270264, "
            "u'3': 0.5682819383259912, u'2': 0.0, u'4': 0.109375}, u'precision': {u'1': 0, u'0': 0.9390467461044913, u'3': 0.33858267716535434, "
            "u'2': 0, "
            "u'4': 0.9130434782608695}, u'falseNegatives': {u'1': 119, u'0': 35, u'3': 98, u'2': 97, u'4': 171}, u'falsePositives': {u'0': 266, "
            "u'3': 252, "
            "u'4': 2}}, u'falseNegatives': 520, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4248}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 43, u'type': u'duration', u'iteration': 414348}",
            "{u'name': u'LossDev', u'iteration': 376680, u'subtype': u'evaluation', u'epoch': 39, u'values': {u'loss': 0.25948768854141235, "
            "u'accumLoss': "
            "1237.237298965454, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 31, u'iteration': 291927}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 57, u'type': u'duration', u'iteration': 546186}",
            "{u'name': u'AccDev', u'iteration': 197757, u'subtype': u'evaluation', u'epoch': 20, u'values': {u'accumAccuracy': 4228.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.886744966442953}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 68, u'type': u'duration', u'iteration': 649773}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 91, u'type': u'duration', u'iteration': 866364}",
            "{u'name': u'CustomMetricDev', u'iteration': 894615, u'subtype': u'evaluation', u'epoch': 94, u'values': {u'truePositives': 136, "
            "u'numExamples': "
            "488, u'micro': {u'recall': 0.4459016393442623, u'precision': 0.4263322884012539, u'f': 0.4358974358974359}, u'macro': {u'recall': "
            "0.39926289926289926, u'precision': 0.34799185294909774, u'f': 0.3718684577569813}, u'perLabel': {u'truePositives': {u'1': 24, "
            "u'3': 72, u'2': 0, "
            "u'4': 40}, u'f': {u'1': 0.39669421487603307, u'3': 0.4800000000000001, u'2': 0, u'4': 0.5517241379310346}, u'recall': {u'1': "
            "0.32432432432432434, "
            "u'3': 0.6666666666666666, u'2': 0.0, u'4': 0.6060606060606061}, u'precision': {u'1': 0.5106382978723404, u'3': 0.375, u'2': 0.0, "
            "u'4': 0.5063291139240507}, u'falseNegatives': {u'1': 50, u'3': 36, u'2': 57, u'4': 26}, u'falsePositives': {u'1': 23, u'3': 120, "
            "u'2': 1, "
            "u'4': 39}}, u'falseNegatives': 169, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 136}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 376680, u'subtype': u'train', u'epoch': 39, u'values': {u'loss': 0.2296602091292389, "
            "u'accumLoss': "
            "17301.451854751213, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 99, u'iteration': 932283}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 93, u'type': u'duration', u'iteration': 885198}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 80, u'type': u'duration', u'iteration': 762777}", u'Number of examples: 75335',
            "{u'duration': 13, u'subtype': u'training', u'epoch': 10, u'type': u'duration', u'iteration': 103587}",
            "{u'name': u'AccDev', u'iteration': 800445, u'subtype': u'evaluation', u'epoch': 84, u'values': {u'accumAccuracy': 4434.0, "
            "u'numExamples': 4768, "
            "u'accuracy': 0.9299496644295302}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 593271, u'subtype': u'train', u'epoch': 62, u'values': {u'loss': 0.18206272512045735, "
            "u'accumLoss': "
            "13715.695396949654, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 42, u'type': u'duration', u'iteration': 404931}",
            "{u'name': u'LossDev', u'iteration': 357846, u'subtype': u'evaluation', u'epoch': 37, u'values': {u'loss': 0.26387837529182434, "
            "u'accumLoss': "
            "1258.1720933914185, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 508518, u'subtype': u'evaluation', u'epoch': 53, u'values': {u'truePositives': 97, "
            "u'numExamples': "
            "413, u'micro': {u'recall': 0.532967032967033, u'precision': 0.29573170731707316, u'f': 0.3803921568627451}, u'macro': {u'recall': "
            "0.27462121212121215, u'precision': 0.1782030620467365, u'f': 0.2161471621321941}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 63, "
            "u'2': 0, "
            "u'4': 34}, u'f': {u'1': 0, u'3': 0.34710743801652894, u'2': 0, u'4': 0.48920863309352514}, u'recall': {u'1': 0.0, "
            "u'3': 0.5833333333333334, "
            "u'2': 0.0, u'4': 0.5151515151515151}, u'precision': {u'1': 0, u'3': 0.24705882352941178, u'2': 0, u'4': 0.4657534246575342}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 45, u'2': 4, u'4': 32}, u'falsePositives': {u'3': 192, u'4': 39}}, u'falseNegatives': 85, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 97}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 932283, u'subtype': u'evaluation', u'epoch': 98, u'values': {u'truePositives': 4453, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9339345637583892, u'precision': 0.9339345637583892, u'f': 0.9339345637583892}, u'macro': {u'recall': "
            "0.5931247420453956, "
            "u'precision': 0.7448963526281713, u'f': 0.6604028273723574}, u'perLabel': {u'truePositives': {u'1': 35, u'0': 4070, u'3': 182, u'2': 4, "
            "u'4': 162}, u'f': {u'1': 0.411764705882353, u'0': 0.9775429326287978, u'3': 0.6606170598911071, u'2': 0.07766990291262137, "
            "u'4': 0.8415584415584416}, u'recall': {u'1': 0.29411764705882354, u'0': 0.9847568352286474, u'3': 0.801762114537445, "
            "u'2': 0.041237113402061855, "
            "u'4': 0.84375}, u'precision': {u'1': 0.6862745098039216, u'0': 0.9704339532665713, u'3': 0.5617283950617284, u'2': 0.6666666666666666, "
            "u'4': 0.8393782383419689}, u'falseNegatives': {u'1': 84, u'0': 63, u'3': 45, u'2': 93, u'4': 30}, u'falsePositives': {u'1': 16, "
            "u'0': 124, "
            "u'3': 142, u'2': 2, u'4': 31}}, u'falseNegatives': 315, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4453}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 27, u'type': u'duration', u'iteration': 263676}",
            "{u'duration': 6, u'subtype': u'training', u'epoch': 75, u'type': u'duration', u'iteration': 715692}",
            "{u'learn_rate': [0.001], u'epoch': 76, u'iteration': 715692}",
            "{u'name': u'LossTrain', u'iteration': 18834, u'subtype': u'train', u'epoch': 1, u'values': {u'loss': 0.5296226250616598, u'accumLoss': "
            "39899.12045902014, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 46, u'type': u'duration', u'iteration': 442599}",
            "{u'name': u'LossDev', u'iteration': 226008, u'subtype': u'evaluation', u'epoch': 23, u'values': {u'loss': 0.30002152919769287, "
            "u'accumLoss': "
            "1430.5026512145996, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 97, u'type': u'duration', u'iteration': 922866}",
            "{u'learn_rate': [0.001], u'epoch': 57, u'iteration': 536769}",
            "{u'name': u'LossTrain', u'iteration': 612105, u'subtype': u'train', u'epoch': 64, u'values': {u'loss': 0.17908594255089647, "
            "u'accumLoss': "
            "13491.439482071786, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 555603, u'subtype': u'evaluation', u'epoch': 58, u'values': {u'loss': 0.22221478819847107, "
            "u'accumLoss': "
            "1059.52011013031, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 555603, u'subtype': u'train', u'epoch': 58, u'values': {u'loss': 0.18837770168955742, "
            "u'accumLoss': "
            "14191.434156782809, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 819279, u'subtype': u'evaluation', u'epoch': 86, u'values': {u'loss': 0.19684141874313354, "
            "u'accumLoss': "
            "938.5398845672607, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 527352, u'subtype': u'evaluation', u'epoch': 55, u'values': {u'loss': 0.2264523059129715, "
            "u'accumLoss': "
            "1079.724594593048, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 197757, u'subtype': u'train', u'epoch': 20, u'values': {u'loss': 0.28604499803802363, "
            "u'accumLoss': "
            "21549.19992719451, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 536769, u'subtype': u'evaluation', u'epoch': 56, u'values': {u'truePositives': 103, "
            "u'numExamples': "
            "412, u'micro': {u'recall': 0.5659340659340659, u'precision': 0.30930930930930933, u'f': 0.4}, u'macro': {u'recall': 0.2914562289562289, "
            "u'precision': 0.1862934362934363, u'f': 0.22730055663359972}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 67, u'2': 0, u'4': 36}, "
            "u'f': {u'1': 0, u'3': 0.36512261580381467, u'2': 0, u'4': 0.5142857142857143}, u'recall': {u'1': 0.0, u'3': 0.6203703703703703, "
            "u'2': 0.0, "
            "u'4': 0.5454545454545454}, u'precision': {u'1': 0, u'3': 0.25868725868725867, u'2': 0, u'4': 0.4864864864864865}, u'falseNegatives': {"
            "u'1': 4, "
            "u'3': 41, u'2': 4, u'4': 30}, u'falsePositives': {u'3': 192, u'4': 38}}, u'falseNegatives': 79, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': "
            "103}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 489684, u'subtype': u'evaluation', u'epoch': 51, u'values': {u'truePositives': 4384, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9194630872483222, u'precision': 0.9194630872483222, u'f': 0.9194630872483222}, u'macro': {u'recall': "
            "0.49061083932624944, "
            "u'precision': 0.4545231716894115, u'f': 0.47187804513803727}, u'perLabel': {u'truePositives': {u'0': 4076, u'3': 171, u'4': 137}, "
            "u'f': {u'1': 0, "
            "u'0': 0.9752362722813733, u'3': 0.5606557377049181, u'2': 0, u'4': 0.7806267806267807}, u'recall': {u'1': 0.0, "
            "u'0': 0.9862085652068715, "
            "u'3': 0.7533039647577092, u'2': 0.0, u'4': 0.7135416666666666}, u'precision': {u'1': 0, u'0': 0.9645054424988169, "
            "u'3': 0.4464751958224543, "
            "u'2': 0, u'4': 0.8616352201257862}, u'falseNegatives': {u'1': 119, u'0': 57, u'3': 56, u'2': 97, u'4': 55}, u'falsePositives': {u'0': "
            "150, "
            "u'3': 212, u'4': 22}}, u'falseNegatives': 384, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4384}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 791028, u'subtype': u'train', u'epoch': 83, u'values': {u'loss': 0.1580972870620083, "
            "u'accumLoss': "
            "11910.259120816394, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 678024, u'subtype': u'evaluation', u'epoch': 71, u'values': {u'truePositives': 113, "
            "u'numExamples': "
            "456, u'micro': {u'recall': 0.44841269841269843, u'precision': 0.35646687697160884, u'f': 0.39718804920913886}, u'macro': {u'recall': "
            "0.32245882245882246, u'precision': 0.41483770550009497, u'f': 0.3628610008442466}, u'perLabel': {u'truePositives': {u'1': 6, u'3': 70, "
            "u'2': 0, "
            "u'4': 37}, u'f': {u'1': 0.14814814814814817, u'3': 0.4057971014492754, u'2': 0, u'4': 0.5323741007194245}, u'recall': {u'1': "
            "0.08108108108108109, "
            "u'3': 0.6481481481481481, u'2': 0.0, u'4': 0.5606060606060606}, u'precision': {u'1': 0.8571428571428571, u'3': 0.29535864978902954, "
            "u'2': 0, "
            "u'4': 0.5068493150684932}, u'falseNegatives': {u'1': 68, u'3': 38, u'2': 4, u'4': 29}, u'falsePositives': {u'1': 1, u'3': 167, "
            "u'4': 36}}, "
            "u'falseNegatives': 139, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 113}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 602688, u'subtype': u'evaluation', u'epoch': 63, u'values': {u'truePositives': 4401, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9230285234899329, u'precision': 0.9230285234899329, u'f': 0.9230285234899329}, u'macro': {u'recall': "
            "0.5083157406700469, "
            "u'precision': 0.664556944799761, u'f': 0.5760297085919472}, u'perLabel': {u'truePositives': {u'1': 1, u'0': 4076, u'3': 175, "
            "u'4': 149}, "
            "u'f': {u'1': 0.016666666666666666, u'0': 0.975936789177541, u'3': 0.5756578947368421, u'2': 0, u'4': 0.8324022346368715}, "
            "u'recall': {u'1': "
            "0.008403361344537815, u'0': 0.9862085652068715, u'3': 0.7709251101321586, u'2': 0.0, u'4': 0.7760416666666666}, u'precision': {u'1': "
            "1.0, "
            "u'0': 0.9658767772511848, u'3': 0.45931758530183725, u'2': 0, u'4': 0.8975903614457831}, u'falseNegatives': {u'1': 118, u'0': 57, "
            "u'3': 52, "
            "u'2': 97, u'4': 43}, u'falsePositives': {u'0': 144, u'3': 206, u'4': 17}}, u'falseNegatives': 367, u'beta': 1.0, u'numLabels': 5, "
            "u'falsePositives': 4401}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 94170, u'subtype': u'evaluation', u'epoch': 9, u'values': {u'truePositives': 4176, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8758389261744967, u'precision': 0.8758389261744967, u'f': 0.8758389261744967}, u'macro': {u'recall': "
            "0.25672121697672506, "
            "u'precision': 0.4501833362130766, u'f': 0.32697940171346607}, u'perLabel': {u'truePositives': {u'1': 2, u'0': 4115, u'3': 45, "
            "u'4': 14}, "
            "u'f': {u'1': 0.025316455696202535, u'0': 0.9463033229849375, u'3': 0.23809523809523808, u'2': 0, u'4': 0.13592233009708737}, "
            "u'recall': {u'1': "
            "0.01680672268907563, u'0': 0.9956448100653279, u'3': 0.19823788546255505, u'2': 0.0, u'4': 0.07291666666666667}, u'precision': {u'1': "
            "0.05128205128205128, u'0': 0.9016213847502191, u'3': 0.2980132450331126, u'2': 0, u'4': 1.0}, u'falseNegatives': {u'1': 117, u'0': 18, "
            "u'3': 182, "
            "u'2': 97, u'4': 178}, u'falsePositives': {u'1': 37, u'0': 449, u'3': 106}}, u'falseNegatives': 592, u'beta': 1.0, u'numLabels': 5, "
            "u'falsePositives': 4176}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 734526, u'subtype': u'evaluation', u'epoch': 77, u'values': {u'loss': 0.20177745819091797, "
            "u'accumLoss': "
            "962.0749206542969, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 37, u'type': u'duration', u'iteration': 357846}",
            "{u'name': u'AccTrain', u'iteration': 160089, u'subtype': u'train', u'epoch': 16, u'values': {u'accumAccuracy': 67124.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.891006836131944}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 9417, u'subtype': u'evaluation', u'epoch': 0, u'values': {u'truePositives': 4133, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8668204697986577, u'precision': 0.8668204697986577, u'f': 0.8668204697986577}, u'macro': {u'recall': 0.2, "
            "u'precision': "
            "0.17336409395973154, u'f': 0.18573194023143466}, u'perLabel': {u'truePositives': {u'0': 4133}, u'f': {u'1': 0, "
            "u'0': 0.9286597011571733, u'3': 0, "
            "u'2': 0, u'4': 0}, u'recall': {u'1': 0.0, u'0': 1.0, u'3': 0.0, u'2': 0.0, u'4': 0.0}, u'precision': {u'1': 0, "
            "u'0': 0.8668204697986577, u'3': 0, "
            "u'2': 0, u'4': 0}, u'falseNegatives': {u'1': 119, u'3': 227, u'2': 97, u'4': 192}, u'falsePositives': {u'0': 635}}, u'falseNegatives': "
            "635, "
            "u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4133}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 96, u'type': u'duration', u'iteration': 913449}",
            "{u'name': u'AccTrain', u'iteration': 847530, u'subtype': u'train', u'epoch': 89, u'values': {u'accumAccuracy': 71071.0, "
            "u'numExamples': 75335, "
            "u'accuracy': 0.9433994823123383}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 640356, u'subtype': u'train', u'epoch': 67, u'values': {u'loss': 0.17500615361805746, "
            "u'accumLoss': "
            "13184.08858281636, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 291927, u'subtype': u'evaluation', u'epoch': 30, u'values': {u'truePositives': 63, "
            "u'numExamples': "
            "451, u'micro': {u'recall': 0.34615384615384615, u'precision': 0.1897590361445783, u'f': 0.245136186770428}, u'macro': {u'recall': "
            "0.16645622895622897, u'precision': 0.09787210338680927, u'f': 0.12326655342144607}, u'perLabel': {u'truePositives': {u'1': 0, "
            "u'3': 49, u'2': 0, "
            "u'4': 14}, u'f': {u'1': 0, u'3': 0.2634408602150538, u'2': 0, u'4': 0.20895522388059704}, u'recall': {u'1': 0.0, "
            "u'3': 0.4537037037037037, "
            "u'2': 0.0, u'4': 0.21212121212121213}, u'precision': {u'1': 0, u'3': 0.1856060606060606, u'2': 0, u'4': 0.20588235294117646}, "
            "u'falseNegatives': {"
            "u'1': 4, u'3': 59, u'2': 4, u'4': 52}, u'falsePositives': {u'3': 215, u'4': 54}}, u'falseNegatives': 119, u'beta': 1.0, u'numLabels': "
            "4, "
            "u'falsePositives': 63}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 612105, u'subtype': u'evaluation', u'epoch': 64, u'values': {u'loss': 0.21395708620548248, "
            "u'accumLoss': "
            "1020.1473870277405, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 85, u'iteration': 800445}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 56, u'type': u'duration', u'iteration': 536769}",
            "{u'name': u'FMetricDev', u'iteration': 885198, u'subtype': u'evaluation', u'epoch': 93, u'values': {u'truePositives': 4444, "
            "u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9320469798657718, u'precision': 0.9320469798657718, u'f': 0.9320469798657718}, u'macro': {u'recall': "
            "0.5763133486225012, "
            "u'precision': 0.606489072306701, u'f': 0.591016288061775}, u'perLabel': {u'truePositives': {u'1': 30, u'0': 4070, u'3': 183, "
            "u'4': 161}, "
            "u'f': {u'1': 0.36809815950920244, u'0': 0.9776603411001681, u'3': 0.647787610619469, u'2': 0, u'4': 0.8385416666666666}, "
            "u'recall': {u'1': "
            "0.25210084033613445, u'0': 0.9847568352286474, u'3': 0.8061674008810573, u'2': 0.0, u'4': 0.8385416666666666}, u'precision': {u'1': "
            "0.6818181818181818, u'0': 0.9706653947054615, u'3': 0.5414201183431953, u'2': 0.0, u'4': 0.8385416666666666}, u'falseNegatives': {"
            "u'1': 89, "
            "u'0': 63, u'3': 44, u'2': 97, u'4': 31}, u'falsePositives': {u'1': 14, u'0': 123, u'3': 155, u'2': 1, u'4': 31}}, u'falseNegatives': "
            "324, "
            "u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4444}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 593271, u'subtype': u'evaluation', u'epoch': 62, u'values': {u'loss': 0.2168954461812973, u'accumLoss': "
            "1034.1574873924255, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 86, u'iteration': 809862}",
            "{u'name': u'LossDev', u'iteration': 282510, u'subtype': u'evaluation', u'epoch': 29, u'values': {u'loss': 0.28471291065216064, u'accumLoss': "
            "1357.511157989502, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 762777, u'subtype': u'evaluation', u'epoch': 80, u'values': {u'accumAccuracy': 4423.0, u'numExamples': 4768, "
            "u'accuracy': 0.9276426174496645}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 781611, u'subtype': u'evaluation', u'epoch': 82, u'values': {u'accumAccuracy': 4428.0, u'numExamples': 4768, "
            "u'accuracy': 0.9286912751677853}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 39, u'iteration': 367263}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 66, u'type': u'duration', u'iteration': 630939}",
            "{u'name': u'AccDev', u'iteration': 357846, u'subtype': u'evaluation', u'epoch': 37, u'values': {u'accumAccuracy': 4349.0, u'numExamples': 4768, "
            "u'accuracy': 0.9121224832214765}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 40, u'type': u'duration', u'iteration': 386097}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 49, u'type': u'duration', u'iteration': 470850}",
            "{u'name': u'AccTrain', u'iteration': 310761, u'subtype': u'train', u'epoch': 32, u'values': {u'accumAccuracy': 69013.0, u'numExamples': 75335, "
            "u'accuracy': 0.9160815026216235}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 37, u'iteration': 348429}",
            "{u'name': u'FMetricDev', u'iteration': 753360, u'subtype': u'evaluation', u'epoch': 79, u'values': {u'truePositives': 4428, u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9286912751677853, u'precision': 0.9286912751677853, u'f': 0.9286912751677853}, u'macro': {u'recall': 0.5402598313665126, "
            "u'precision': 0.6050924560334034, u'f': 0.5708412195166136}, u'perLabel': {u'truePositives': {u'1': 15, u'0': 4081, u'3': 176, u'4': 156}, "
            "u'f': {u'1': 0.21276595744680848, u'0': 0.9770169978453436, u'3': 0.6153846153846153, u'2': 0, u'4': 0.8387096774193549}, u'recall': {u'1': "
            "0.12605042016806722, u'0': 0.9874183401887249, u'3': 0.775330396475771, u'2': 0.0, u'4': 0.8125}, u'precision': {u'1': 0.6818181818181818, "
            "u'0': 0.966832504145937, u'3': 0.5101449275362319, u'2': 0, u'4': 0.8666666666666667}, u'falseNegatives': {u'1': 104, u'0': 52, u'3': 51, "
            "u'2': 97, u'4': 36}, u'falsePositives': {u'1': 7, u'0': 140, u'3': 169, u'4': 24}}, u'falseNegatives': 340, u'beta': 1.0, u'numLabels': 5, "
            "u'falsePositives': 4428}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 178923, u'subtype': u'evaluation', u'epoch': 18, u'values': {u'loss': 0.3136332929134369, u'accumLoss': "
            "1495.403540611267, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 772194, u'subtype': u'evaluation', u'epoch': 81, u'values': {u'accumAccuracy': 4423.0, u'numExamples': 4768, "
            "u'accuracy': 0.9276426174496645}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 70, u'type': u'duration', u'iteration': 668607}",
            "{u'learn_rate': [0.001], u'epoch': 36, u'iteration': 339012}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 16, u'type': u'duration', u'iteration': 160089}",
            "{u'name': u'AccDev', u'iteration': 602688, u'subtype': u'evaluation', u'epoch': 63, u'values': {u'accumAccuracy': 4401.0, u'numExamples': 4768, "
            "u'accuracy': 0.9230285234899329}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 55, u'type': u'duration', u'iteration': 527352}",
            "{u'name': u'CustomMetricDev', u'iteration': 367263, u'subtype': u'evaluation', u'epoch': 38, u'values': {u'truePositives': 81, u'numExamples': "
            "448, u'micro': {u'recall': 0.44505494505494503, u'precision': 0.2334293948126801, u'f': 0.30623818525519847}, u'macro': {u'recall': "
            "0.22432659932659932, u'precision': 0.12979207277452892, u'f': 0.16444100014441349}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 56, u'2': 0, "
            "u'4': 25}, u'f': {u'1': 0, u'3': 0.2994652406417112, u'2': 0, u'4': 0.34013605442176875}, u'recall': {u'1': 0.0, u'3': 0.5185185185185185, "
            "u'2': 0.0, u'4': 0.3787878787878788}, u'precision': {u'1': 0, u'3': 0.21052631578947367, u'2': 0, u'4': 0.30864197530864196}, u'falseNegatives': {"
            "u'1': 4, u'3': 52, u'2': 4, u'4': 41}, u'falsePositives': {u'3': 210, u'4': 56}}, u'falseNegatives': 101, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 81}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 612105, u'subtype': u'evaluation', u'epoch': 64, u'values': {u'truePositives': 106, u'numExamples': "
            "465, u'micro': {u'recall': 0.42063492063492064, u'precision': 0.3322884012539185, u'f': 0.3712784588441331}, u'macro': {u'recall': "
            "0.3024103649103649, u'precision': 0.4516165820835947, u'f': 0.36225107320618266}, u'perLabel': {u'truePositives': {u'1': 1, u'3': 67, u'2': 0, "
            "u'4': 38}, u'f': {u'1': 0.026666666666666665, u'3': 0.37746478873239436, u'2': 0, u'4': 0.5547445255474452}, u'recall': {u'1': "
            "0.013513513513513514, u'3': 0.6203703703703703, u'2': 0.0, u'4': 0.5757575757575758}, u'precision': {u'1': 1.0, u'3': 0.27125506072874495, "
            "u'2': 0, u'4': 0.5352112676056338}, u'falseNegatives': {u'1': 73, u'3': 41, u'2': 4, u'4': 28}, u'falsePositives': {u'1': 0, u'3': 180, "
            "u'4': 33}}, u'falseNegatives': 146, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 106}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 480267, u'subtype': u'evaluation', u'epoch': 50, u'values': {u'loss': 0.23562993109226227, u'accumLoss': "
            "1123.4835114479065, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 461433, u'subtype': u'train', u'epoch': 48, u'values': {u'loss': 0.207633363227143, u'accumLoss': "
            "15642.059418716817, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 94, u'type': u'duration', u'iteration': 894615}",
            "{u'name': u'FMetricDev', u'iteration': 320178, u'subtype': u'evaluation', u'epoch': 33, u'values': {u'truePositives': 4336, u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9093959731543624, u'precision': 0.9093959731543624, u'f': 0.9093959731543624}, u'macro': {u'recall': 0.44103342896062736, "
            "u'precision': 0.4320896844499231, u'f': 0.43651574955354366}, u'perLabel': {u'truePositives': {u'0': 4078, u'3': 156, u'4': 102}, u'f': {u'1': 0, "
            "u'0': 0.9716464141053134, u'3': 0.5157024793388431, u'2': 0, u'4': 0.6355140186915887}, u'recall': {u'1': 0.0, u'0': 0.9866924751996129, "
            "u'3': 0.6872246696035242, u'2': 0.0, u'4': 0.53125}, u'precision': {u'1': 0, u'0': 0.957052335132598, u'3': 0.4126984126984127, u'2': 0, "
            "u'4': 0.7906976744186046}, u'falseNegatives': {u'1': 119, u'0': 55, u'3': 71, u'2': 97, u'4': 90}, u'falsePositives': {u'0': 183, u'3': 222, "
            "u'4': 27}}, u'falseNegatives': 432, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4336}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 13, u'type': u'duration', u'iteration': 131838}",
            "{u'name': u'AccTrain', u'iteration': 28251, u'subtype': u'train', u'epoch': 2, u'values': {u'accumAccuracy': 65313.0, u'numExamples': 75335, "
            "u'accuracy': 0.8669675449658193}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 58, u'iteration': 546186}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 20, u'type': u'duration', u'iteration': 197757}",
            "{u'learn_rate': [0.001], u'epoch': 11, u'iteration': 103587}", "{u'learn_rate': [0.001], u'epoch': 59, u'iteration': 555603}",
            "{u'name': u'AccDev', u'iteration': 583854, u'subtype': u'evaluation', u'epoch': 61, u'values': {u'accumAccuracy': 4400.0, u'numExamples': 4768, "
            "u'accuracy': 0.9228187919463087}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 423765, u'subtype': u'train', u'epoch': 44, u'values': {u'accumAccuracy': 69634.0, u'numExamples': 75335, "
            "u'accuracy': 0.9243246830822327}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 84753, u'subtype': u'evaluation', u'epoch': 8, u'values': {u'truePositives': 4169, u'numExamples': 4768, "
            "u'micro': {u'recall': 0.8743708053691275, u'precision': 0.8743708053691275, u'f': 0.8743708053691274}, u'macro': {u'recall': 0.24904909295471533, "
            "u'precision': 0.444552864450748, u'f': 0.31924791007231157}, u'perLabel': {u'truePositives': {u'1': 2, u'0': 4117, u'3': 35, u'4': 15}, "
            "u'f': {u'1': 0.024390243902439022, u'0': 0.9446994033960533, u'3': 0.19886363636363638, u'2': 0, u'4': 0.14492753623188406}, u'recall': {u'1': "
            "0.01680672268907563, u'0': 0.9961287200580692, u'3': 0.15418502202643172, u'2': 0.0, u'4': 0.078125}, u'precision': {u'1': 0.044444444444444446, "
            "u'0': 0.8983198778092952, u'3': 0.28, u'2': 0, u'4': 1.0}, u'falseNegatives': {u'1': 117, u'0': 16, u'3': 192, u'2': 97, u'4': 177}, "
            "u'falsePositives': {u'1': 43, u'0': 466, u'3': 90}}, u'falseNegatives': 599, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4169}, "
            "u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 847530, u'subtype': u'evaluation', u'epoch': 89, u'values': {u'truePositives': 128, u'numExamples': "
            "427, u'micro': {u'recall': 0.5079365079365079, u'precision': 0.42244224422442245, u'f': 0.46126126126126127}, u'macro': {u'recall': "
            "0.37395349895349894, u'precision': 0.3483797934059714, u'f': 0.3607139365909972}, u'perLabel': {u'truePositives': {u'1': 19, u'3': 70, u'2': 0, "
            "u'4': 39}, u'f': {u'1': 0.33928571428571425, u'3': 0.46822742474916385, u'2': 0, u'4': 0.5571428571428572}, u'recall': {u'1': 0.25675675675675674, "
            "u'3': 0.6481481481481481, u'2': 0.0, u'4': 0.5909090909090909}, u'precision': {u'1': 0.5, u'3': 0.36649214659685864, u'2': 0, "
            "u'4': 0.527027027027027}, u'falseNegatives': {u'1': 55, u'3': 38, u'2': 4, u'4': 27}, u'falsePositives': {u'1': 19, u'3': 121, u'4': 35}}, "
            "u'falseNegatives': 124, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 128}, u'type': u'metric'}",
            "{u'duration': 6, u'subtype': u'training', u'epoch': 86, u'type': u'duration', u'iteration': 819279}",
            "{u'name': u'LossDev', u'iteration': 517935, u'subtype': u'evaluation', u'epoch': 54, u'values': {u'loss': 0.22911952435970306, u'accumLoss': "
            "1092.4418921470642, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 31, u'type': u'duration', u'iteration': 301344}",
            "{u'name': u'LossTrain', u'iteration': 84753, u'subtype': u'train', u'epoch': 8, u'values': {u'loss': 0.36106018252320166, u'accumLoss': "
            "27200.468850385398, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 913449, u'subtype': u'evaluation', u'epoch': 96, u'values': {u'truePositives': 142, u'numExamples': "
            "483, u'micro': {u'recall': 0.46557377049180326, u'precision': 0.44375, u'f': 0.45439999999999997}, u'macro': {u'recall': 0.4184136289399447, "
            "u'precision': 0.44141541083030444, u'f': 0.42960685292712497}, u'perLabel': {u'truePositives': {u'1': 27, u'3': 74, u'2': 1, u'4': 40}, "
            "u'f': {u'1': 0.4285714285714286, u'3': 0.5, u'2': 0.03333333333333333, u'4': 0.5594405594405594}, u'recall': {u'1': 0.36486486486486486, "
            "u'3': 0.6851851851851852, u'2': 0.017543859649122806, u'4': 0.6060606060606061}, u'precision': {u'1': 0.5192307692307693, "
            "u'3': 0.39361702127659576, u'2': 0.3333333333333333, u'4': 0.5194805194805194}, u'falseNegatives': {u'1': 47, u'3': 34, u'2': 56, u'4': 26}, "
            "u'falsePositives': {u'1': 25, u'3': 114, u'2': 2, u'4': 37}}, u'falseNegatives': 163, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 142}, "
            "u'type': u'metric'}",
            u'Usando o filtro: data.Filters TransformLowerCaseFilter',
            "{u'name': u'LossDev', u'iteration': 254259, u'subtype': u'evaluation', u'epoch': 26, u'values': {u'loss': 0.29146650433540344, u'accumLoss': "
            "1389.7122926712036, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 762777, u'subtype': u'evaluation', u'epoch': 80, u'values': {u'loss': 0.20047740638256073, u'accumLoss': "
            "955.8762736320496, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 77, u'type': u'duration', u'iteration': 734526}",
            "{u'name': u'LossDev', u'iteration': 696858, u'subtype': u'evaluation', u'epoch': 73, u'values': {u'loss': 0.20495958626270294, u'accumLoss': "
            "977.2473073005676, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 1, u'iteration': 9417}",
            "{u'name': u'LossDev', u'iteration': 216591, u'subtype': u'evaluation', u'epoch': 22, u'values': {u'loss': 0.3019566237926483, u'accumLoss': "
            "1439.7291822433472, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 43, u'type': u'duration', u'iteration': 414348}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 40, u'type': u'duration', u'iteration': 386097}",
            "{u'name': u'LossDev', u'iteration': 546186, u'subtype': u'evaluation', u'epoch': 57, u'values': {u'loss': 0.22344233095645905, u'accumLoss': "
            "1065.3730340003967, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 320178, u'subtype': u'evaluation', u'epoch': 33, u'values': {u'accumAccuracy': 4336.0, u'numExamples': 4768, "
            "u'accuracy': 0.9093959731543624}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 866364, u'subtype': u'evaluation', u'epoch': 91, u'values': {u'loss': 0.19336575269699097, u'accumLoss': "
            "921.9679088592529, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 98, u'type': u'duration', u'iteration': 932283}",
            "{u'learn_rate': [0.001], u'epoch': 68, u'iteration': 640356}",
            "{u'name': u'FMetricDev', u'iteration': 301344, u'subtype': u'evaluation', u'epoch': 31, u'values': {u'truePositives': 4324, u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9068791946308725, u'precision': 0.9068791946308725, u'f': 0.9068791946308725}, u'macro': {u'recall': 0.4207182137397041, "
            "u'precision': 0.4442416810787339, u'f': 0.43216007505504084}, u'perLabel': {u'truePositives': {u'0': 4087, u'3': 149, u'4': 88}, u'f': {u'1': 0, "
            "u'0': 0.9691723974389377, u'3': 0.5033783783783784, u'2': 0, u'4': 0.5986394557823129}, u'recall': {u'1': 0.0, u'0': 0.988870070166949, "
            "u'3': 0.6563876651982379, u'2': 0.0, u'4': 0.4583333333333333}, u'precision': {u'1': 0, u'0': 0.9502441292722623, u'3': 0.40821917808219177, "
            "u'2': 0, u'4': 0.8627450980392157}, u'falseNegatives': {u'1': 119, u'0': 46, u'3': 78, u'2': 97, u'4': 104}, u'falsePositives': {u'0': 214, "
            "u'3': 216, u'4': 14}}, u'falseNegatives': 444, u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4324}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 395514, u'subtype': u'train', u'epoch': 41, u'values': {u'loss': 0.2243247421150694, u'accumLoss': "
            "16899.504447238753, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 659190, u'subtype': u'train', u'epoch': 69, u'values': {u'loss': 0.1725555284074335, u'accumLoss': "
            "12999.470732574002, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 376680, u'subtype': u'evaluation', u'epoch': 39, u'values': {u'accumAccuracy': 4357.0, u'numExamples': 4768, "
            "u'accuracy': 0.9138003355704698}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 339012, u'subtype': u'evaluation', u'epoch': 35, u'values': {u'accumAccuracy': 4347.0, u'numExamples': 4768, "
            "u'accuracy': 0.9117030201342282}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 25, u'type': u'duration', u'iteration': 244842}",
            "{u'learn_rate': [0.001], u'epoch': 82, u'iteration': 772194}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 85, u'type': u'duration', u'iteration': 809862}",
            "{u'name': u'CustomMetricDev', u'iteration': 791028, u'subtype': u'evaluation', u'epoch': 83, u'values': {u'truePositives': 123, u'numExamples': "
            "437, u'micro': {u'recall': 0.4880952380952381, u'precision': 0.39935064935064934, u'f': 0.4392857142857142}, u'macro': {u'recall': "
            "0.35599804349804354, u'precision': 0.32907876943881, u'f': 0.34200952612815544}, u'perLabel': {u'truePositives': {u'1': 13, u'3': 71, u'2': 0, "
            "u'4': 39}, u'f': {u'1': 0.25242718446601947, u'3': 0.4551282051282051, u'2': 0, u'4': 0.5531914893617023}, u'recall': {u'1': 0.17567567567567569, "
            "u'3': 0.6574074074074074, u'2': 0.0, u'4': 0.5909090909090909}, u'precision': {u'1': 0.4482758620689655, u'3': 0.3480392156862745, u'2': 0, "
            "u'4': 0.52}, u'falseNegatives': {u'1': 61, u'3': 37, u'2': 4, u'4': 27}, u'falsePositives': {u'1': 16, u'3': 133, u'4': 36}}, u'falseNegatives': "
            "129, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 123}, u'type': u'metric'}",
            "{u'name': u'FMetricDev', u'iteration': 894615, u'subtype': u'evaluation', u'epoch': 94, u'values': {u'truePositives': 4443, u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9318372483221476, u'precision': 0.9318372483221476, u'f': 0.9318372483221476}, u'macro': {u'recall': 0.5795295201624939, "
            "u'precision': 0.6046553505743226, u'f': 0.5918258775996491}, u'perLabel': {u'truePositives': {u'1': 32, u'0': 4067, u'3': 183, u'4': 161}, "
            "u'f': {u'1': 0.38554216867469876, u'0': 0.9777617502103619, u'3': 0.6443661971830986, u'2': 0, u'4': 0.8363636363636363}, u'recall': {u'1': "
            "0.2689075630252101, u'0': 0.9840309702395355, u'3': 0.8061674008810573, u'2': 0.0, u'4': 0.8385416666666666}, u'precision': {u'1': "
            "0.6808510638297872, u'0': 0.9715719063545151, u'3': 0.5366568914956011, u'2': 0.0, u'4': 0.8341968911917098}, u'falseNegatives': {u'1': 87, "
            "u'0': 66, u'3': 44, u'2': 97, u'4': 31}, u'falsePositives': {u'1': 15, u'0': 119, u'3': 158, u'2': 1, u'4': 32}}, u'falseNegatives': 325, "
            "u'beta': 1.0, u'numLabels': 5, u'falsePositives': 4443}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 800445, u'subtype': u'train', u'epoch': 84, u'values': {u'loss': 0.1572195238119066, u'accumLoss': "
            "11844.132826369983, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 828696, u'subtype': u'evaluation', u'epoch': 87, u'values': {u'loss': 0.19523751735687256, u'accumLoss': "
            "930.8924827575684, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 93, u'iteration': 875781}",
            "{u'name': u'AccDev', u'iteration': 753360, u'subtype': u'evaluation', u'epoch': 79, u'values': {u'accumAccuracy': 4428.0, u'numExamples': 4768, "
            "u'accuracy': 0.9286912751677853}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 47085, u'subtype': u'evaluation', u'epoch': 4, u'values': {u'loss': 0.4347775876522064, u'accumLoss': "
            "2073.01953792572, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 489684, u'subtype': u'evaluation', u'epoch': 51, u'values': {u'loss': 0.23317180573940277, u'accumLoss': "
            "1111.7631697654724, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 1, u'type': u'duration', u'iteration': 18834}",
            "{u'name': u'LossTrain', u'iteration': 922866, u'subtype': u'train', u'epoch': 97, u'values': {u'loss': 0.1471927552355457, u'accumLoss': "
            "11088.766215669835, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 320178, u'subtype': u'evaluation', u'epoch': 33, u'values': {u'truePositives': 75, u'numExamples': "
            "462, u'micro': {u'recall': 0.41208791208791207, u'precision': 0.2112676056338028, u'f': 0.2793296089385474}, u'macro': {u'recall': "
            "0.20307239057239057, u'precision': 0.11134191012239793, u'f': 0.14382595072480667}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 55, u'2': 0, "
            "u'4': 20}, u'f': {u'1': 0, u'3': 0.2887139107611549, u'2': 0, u'4': 0.2702702702702703}, u'recall': {u'1': 0.0, u'3': 0.5092592592592593, "
            "u'2': 0.0, u'4': 0.30303030303030304}, u'precision': {u'1': 0, u'3': 0.20146520146520147, u'2': 0, u'4': 0.24390243902439024}, u'falseNegatives': "
            "{u'1': 4, u'3': 53, u'2': 4, u'4': 46}, u'falsePositives': {u'3': 218, u'4': 62}}, u'falseNegatives': 107, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 75}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 376680, u'subtype': u'evaluation', u'epoch': 39, u'values': {u'truePositives': 87, u'numExamples': "
            "450, u'micro': {u'recall': 0.47802197802197804, u'precision': 0.24507042253521127, u'f': 0.32402234636871513}, u'macro': {u'recall': "
            "0.2411616161616162, u'precision': 0.13647236002834867, u'f': 0.17430579333926524}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 60, u'2': 0, "
            "u'4': 27}, u'f': {u'1': 0, u'3': 0.31578947368421056, u'2': 0, u'4': 0.3624161073825503}, u'recall': {u'1': 0.0, u'3': 0.5555555555555556, "
            "u'2': 0.0, u'4': 0.4090909090909091}, u'precision': {u'1': 0, u'3': 0.22058823529411764, u'2': 0, u'4': 0.3253012048192771}, u'falseNegatives': {"
            "u'1': 4, u'3': 48, u'2': 4, u'4': 39}, u'falsePositives': {u'3': 212, u'4': 56}}, u'falseNegatives': 95, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 87}, u'type': u'metric'}",
            "{u'learn_rate': [0.001], u'epoch': 49, u'iteration': 461433}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 5, u'type': u'duration', u'iteration': 56502}",
            "{u'name': u'AccDev', u'iteration': 819279, u'subtype': u'evaluation', u'epoch': 86, u'values': {u'accumAccuracy': 4427.0, u'numExamples': 4768, "
            "u'accuracy': 0.928481543624161}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 668607, u'subtype': u'train', u'epoch': 70, u'values': {u'accumAccuracy': 70530.0, u'numExamples': 75335, "
            "u'accuracy': 0.9362182252605031}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 687441, u'subtype': u'evaluation', u'epoch': 72, u'values': {u'truePositives': 115, u'numExamples': "
            "449, u'micro': {u'recall': 0.45634920634920634, u'precision': 0.3685897435897436, u'f': 0.40780141843971635}, u'macro': {u'recall': "
            "0.32962507962507964, u'precision': 0.4261254789272031, u'f': 0.3717142999952871}, u'perLabel': {u'truePositives': {u'1': 7, u'3': 70, u'2': 0, "
            "u'4': 38}, u'f': {u'1': 0.17073170731707316, u'3': 0.411764705882353, u'2': 0, u'4': 0.5507246376811594}, u'recall': {u'1': 0.0945945945945946, "
            "u'3': 0.6481481481481481, u'2': 0.0, u'4': 0.5757575757575758}, u'precision': {u'1': 0.875, u'3': 0.3017241379310345, u'2': 0, "
            "u'4': 0.5277777777777778}, u'falseNegatives': {u'1': 67, u'3': 38, u'2': 4, u'4': 28}, u'falsePositives': {u'1': 1, u'3': 162, u'4': 34}}, "
            "u'falseNegatives': 137, u'beta': 1.0, u'numLabels': 4, u'falsePositives': 115}, u'type': u'metric'}",
            "{u'name': u'AccTrain', u'iteration': 536769, u'subtype': u'train', u'epoch': 56, u'values': {u'accumAccuracy': 70137.0, u'numExamples': 75335, "
            "u'accuracy': 0.9310015265149001}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 11, u'type': u'duration', u'iteration': 113004}",
            "{u'name': u'LossDev', u'iteration': 904032, u'subtype': u'evaluation', u'epoch': 95, u'values': {u'loss': 0.19126580655574799, u'accumLoss': "
            "911.9553656578064, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 56502, u'subtype': u'train', u'epoch': 5, u'values': {u'loss': 0.4158907300587109, u'accumLoss': "
            "31331.128148972988, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 753360, u'subtype': u'evaluation', u'epoch': 79, u'values': {u'loss': 0.20036646723747253, u'accumLoss': "
            "955.347315788269, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 131838, u'subtype': u'train', u'epoch': 13, u'values': {u'loss': 0.31726384436767424, u'accumLoss': "
            "23901.07171543874, u'numExamples': 75335}, u'type': u'metric'}",
            u'Loading word embedding...', "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 64, u'type': u'duration', u'iteration': 612105}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 13, u'type': u'duration', u'iteration': 131838}",
            "{u'name': u'AccTrain', u'iteration': 885198, u'subtype': u'train', u'epoch': 93, u'values': {u'accumAccuracy': 71159.0, u'numExamples': 75335, "
            "u'accuracy': 0.9445675980619898}, u'type': u'metric'}",
            "{u'name': u'CustomMetricDev', u'iteration': 386097, u'subtype': u'evaluation', u'epoch': 40, u'values': {u'truePositives': 81, u'numExamples': "
            "442, u'micro': {u'recall': 0.44505494505494503, u'precision': 0.2375366568914956, u'f': 0.30975143403441685}, u'macro': {u'recall': "
            "0.2257996632996633, u'precision': 0.1323570957717299, u'f': 0.1668888658589885}, u'perLabel': {u'truePositives': {u'1': 0, u'3': 55, u'2': 0, "
            "u'4': 26}, u'f': {u'1': 0, u'3': 0.2997275204359673, u'2': 0, u'4': 0.35135135135135137}, u'recall': {u'1': 0.0, u'3': 0.5092592592592593, "
            "u'2': 0.0, u'4': 0.3939393939393939}, u'precision': {u'1': 0, u'3': 0.21235521235521235, u'2': 0, u'4': 0.3170731707317073}, u'falseNegatives': {"
            "u'1': 4, u'3': 53, u'2': 4, u'4': 40}, u'falsePositives': {u'3': 204, u'4': 56}}, u'falseNegatives': 101, u'beta': 1.0, u'numLabels': 4, "
            "u'falsePositives': 81}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 4, u'type': u'duration', u'iteration': 47085}", u'device=cuda',
            "{u'name': u'LossDev', u'iteration': 9417, u'subtype': u'evaluation', u'epoch': 0, u'values': {u'loss': 0.5454654097557068, u'accumLoss': "
            "2600.77907371521, u'numExamples': 4768}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 649773, u'subtype': u'train', u'epoch': 68, u'values': {u'loss': 0.1737818054452079, u'accumLoss': "
            "13091.852313214738, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'AccDev', u'iteration': 273093, u'subtype': u'evaluation', u'epoch': 28, u'values': {u'accumAccuracy': 4300.0, u'numExamples': 4768, "
            "u'accuracy': 0.9018456375838926}, u'type': u'metric'}",
            "{u'duration': 0, u'subtype': u'evaluation', u'epoch': 36, u'type': u'duration', u'iteration': 348429}",
            "{u'name': u'FMetricDev', u'iteration': 847530, u'subtype': u'evaluation', u'epoch': 89, u'values': {u'truePositives': 4442, u'numExamples': 4768, "
            "u'micro': {u'recall': 0.9316275167785235, u'precision': 0.9316275167785235, u'f': 0.9316275167785235}, u'macro': {u'recall': 0.5635706101326556, "
            "u'precision': 0.6047352028402532, u'f': 0.5834277009478163}, u'perLabel': {u'truePositives': {u'1': 25, u'0': 4078, u'3': 180, u'4': 159}, "
            "u'f': {u'1': 0.3184713375796179, u'0': 0.9778204052271909, u'3': 0.6371681415929203, u'2': 0, u'4': 0.8457446808510638}, u'recall': {u'1': "
            "0.21008403361344538, u'0': 0.9866924751996129, u'3': 0.7929515418502202, u'2': 0.0, u'4': 0.828125}, u'precision': {u'1': 0.6578947368421053, "
            "u'0': 0.969106463878327, u'3': 0.5325443786982249, u'2': 0, u'4': 0.8641304347826086}, u'falseNegatives': {u'1': 94, u'0': 55, u'3': 47, u'2': 97, "
            "u'4': 33}, u'falsePositives': {u'1': 13, u'0': 130, u'3': 158, u'4': 25}}, u'falseNegatives': 326, u'beta': 1.0, u'numLabels': 5, "
            "u'falsePositives': 4442}, u'type': u'metric'}",
            "{u'duration': 7, u'subtype': u'training', u'epoch': 99, u'type': u'duration', u'iteration': 941700}",
            "{u'name': u'LossTrain', u'iteration': 602688, u'subtype': u'train', u'epoch': 63, u'values': {u'loss': 0.18056327586718912, u'accumLoss': "
            "13602.734387454693, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossTrain', u'iteration': 678024, u'subtype': u'train', u'epoch': 71, u'values': {u'loss': 0.17018041042681545, u'accumLoss': "
            "12820.541219504143, u'numExamples': 75335}, u'type': u'metric'}",
            "{u'name': u'LossDev', u'iteration': 150672, u'subtype': u'evaluation', u'epoch': 15, u'values': {u'loss': 0.3243519961833954, u'accumLoss': "
            "1546.5103178024292, u'numExamples': 4768}, u'type': u'metric'}"},
        u'module': set([u'model.BasicModel', u'data.Lexicon', u'data.TokenDatasetReader', u'data.BatchIterator', u'__main__']),
        u'level': set([u'INFO', u'WARNING'])}}


class montaTree:

    def __init__(self):
        self.numProperties = {}

    def buildJsonSet(self, dictionary):

        if isinstance(dictionary, dict):
            self.dict_generator(indict=dictionary)

        elif isinstance(dictionary, set):
            for i in dictionary:
                self.generate(i)

        elif isinstance(dictionary, list):
            print(dictionary)

        elif isinstance(dictionary, str):
            z = ast.literal_eval(dictionary)
            self.dict_generator(indict=z)


    def generate(self, dictionary, key=None):
        conjuntos = dict()
        builded = None

        try:
            z = ast.literal_eval(dictionary)
        except Exception as error:
            z = dictionary
        if not isinstance(z, unicode):

            for k, v in z.iteritems():
                logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
                logging.debug(type(v))
                if isinstance(v, list) and len(v) == 1:
                    v = v[0]
                if isinstance(v, dict):
                    builded = self.generate(dictionary=v, key=k)
                    conjuntos[k] = builded
                    builded = None
                if builded != None:
                    if not k in conjuntos['message']:
                        conjuntos[k] = set()
                    conjuntos['message'][k].add(str(v))
        return conjuntos

    def dict_generator(self, indict, pre=None):
        pre = pre[:] if pre else []
        if isinstance(indict, dict):
            for key, value in indict.items():
                if isinstance(value, dict):
                    for d in self.dict_generator(value, [key] + pre):
                        yield d
                elif isinstance(value, list) or isinstance(value, tuple):
                    for v in value:
                        for d in self.dict_generator(v, [key] + pre):
                            yield d
                else:
                    yield pre + [key, value]
        else:
            yield indict

    def _addPath(self, path):
        d = self.numProperties
        for p in path[:-1]:
            d = d.setdefault(p, {})
        numProp = path[-1]
        d.setdefault(numProp, None)

    def fillNumProperties(self, d, path=[]):
        if isinstance(d, dict):
            for key, val in d.items():
                self.fillNumProperties(val, path + [key])
        elif isinstance(d, (float, int)):
            self._addPath(path)


teste =  {'macro': {'recall':
            "0.20686026936026936", 'precision': 0.11738162212845757, 'f': 0.14977456404507988}, 'perLabel': {'truePositives': {'1': 0,
            '3': 55, '2': 0,
            '4': 21}, 'f': {'1': 0, '3': 0.291005291005291, '2': 0, '4': 0.28965517241379307},  'recall': {'1': 0.0,
            '3': 0.5092592592592593,
            '2': 0.0, '4': 0.3181818181818182}, 'precision': {'1': 0, '3': 0.2037037037037037, '2': 0, '4': 0.26582278481012656},
            'falseNegatives': {'1': 4, '3': 53, '2': 4, '4': 45}, 'falsePositives': {'3': 215, '4': 58}}}
execute = dict()
mt = montaTree()
for i in arquivo['wnn-harem_second-epochs_100-batch_size_8-hidden_size_100.log']['message']:
    if isinstance(i, unicode) and ":" in i:
        j = i.split(":")
        i = str("{'"+j[0]+"'"+":'"+j[1]+"'}")
    if not isinstance(i, unicode):
        mt.fillNumProperties(ast.literal_eval(i))

print json.dumps(mt.numProperties, indent=2)

#             if i != 0.001:
#                 if len(i) == 2:
#                     if not i[0] in execute:
#                         execute[i[0]] = set()
#                         execute[i[0]].add(i[1])
#
#                 elif len(i) == 3:
#                     if not i[0] in execute:
#                         execute[i[0]] = dict()
#                         if not i[1] in execute[i[0]]:
#                             execute[i[0]][i[1]] = set()
#                             execute[i[0]][i[1]].add(i[2])
#
#                 elif len(i) == 4:
#                     if not i[0] in execute:
#                         execute[i[0]] = dict()
#                         if not i[1] in execute[i[0]]:
#                             execute[i[0]][i[1]] = dict()
#                             execute[i[0]][i[1]][i[2]] = set()
#                             execute[i[0]][i[1]][i[2]].add(i[3])
#
#                 elif len(i) == 5:
#                     if not i[0] in execute:
#                         execute[i[0]] = dict()
#                         if not i[1] in execute[i[0]]:
#                             execute[i[0]][i[1]] = dict()
#                             execute[i[0]][i[1]][i[2]] = dict()
#                             execute[i[0]][i[1]][i[2]][i[3]] = set()
#                             execute[i[0]][i[1]][i[2]][i[3]].add(i[4])
#             else:
#                 if not 'learn_rate' in execute:
#                     execute['learn_rate'] = set()
#                 execute['learn_rate'].add(i)
#
# print(json.dumps(repr(execute), indent=4))