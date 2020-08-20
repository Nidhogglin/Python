# 以uid分应用统计流量

import os
import time

path = ''
# C:\\Users\\linzr\\Desktop\\test\\
RATIO = 1024 * 1024

# 抓取并导出车机流量日志到指定文件（与脚本在同一目录）
def bat():

    # 导出流量日志
    os.system('adb wait-for-device')
    os.system('adb root')
    os.system('adb wait-for-device')
    os.system('adb shell \"cat /proc/net/xt_qtaguid/stats\" > flowlog.txt')


# 根据uid记录各应用流量及总流量到指定文档（与脚本在同一目录）
def flow_record():

    # 根据应用uid初始化各应用的流量值
    uid_flow = {}
    file1 = open(path+'flowlog.txt')
    for line in file1.readlines()[1:]:
        if line != '\n' or 'eth0' in line:
            line_list = line.split(' ')
            uid_flow[line_list[3]] = 0
    file1.close()

    # 根据uid计算单应用累计流量总和及所有应用累计流量的总和
    flow_sum = 0
    file2 = open(path+'flowlog.txt')
    for line in file2.readlines()[1:]:
        if line != '\n' or 'eth0' in line:
            line_list = line.split(' ')
            flow_sum += (int(line_list[5]) + int(line_list[7]))
            uid_flow[line_list[3]] += (int(line_list[5]) + int(line_list[7]))
    file2.close()

    return uid_flow, flow_sum  # 单应用累计流量，所有应用累计流量总和


# 设定时间间隔内单应用消耗的流量及所有应用消耗流量的总和
def flow_count():

    # 开始时记录一次累计流量
    bat()
    uid_flow1, flow_sum1 = flow_record()

    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(now_time)

    # 记录第一次读取的流量
    file1 = open(path+'flowcount.txt', 'a')
    file1.write(now_time+'\n')
    file1.write(str(round(flow_sum1 / RATIO, 2))+'M\t')
    for i in uid_flow1:
        file1.write(i+'：'+str(round(uid_flow1[i] / RATIO, 2))+'M, ')
    file1.write('\n')
    file1.close()
    while True:
        
        time.sleep(60 * 0.1)  # 时间间隔，单位为s

        # 第二次记录累计流量
        bat()
        uid_flow2, flow_sum2 = flow_record()

        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(now_time)

        # 把流量计算结果记录到文档
        file1 = open(path+'flowcount.txt', 'a')
        file1.write(now_time+'\n')
        # file1.write(str(flow_sum2) + '\t' + str(uid_flow2) + '\n')
        file1.write('{0}\t'.format(str(round(flow_sum2 / RATIO, 2))))
        for i in uid_flow2:
            file1.write(i+'：'+str(round(uid_flow2[i] / RATIO, 2)) + 'M, ')
        file1.write('\n')

        file1.write('消耗流量：'+str(round((flow_sum2 - flow_sum1) / RATIO, 2))+'M'+'\t')
        flow_sum1 = flow_sum2
        for i in uid_flow2:
            if i not in uid_flow1:
                uid_flow1[i] = 0
            file1.write(i+'：'+str(round((uid_flow2[i] - uid_flow1[i]) / RATIO, 2))+'M, ')
            uid_flow1[i] = uid_flow2[i]
        file1.write('\n')
        file1.close()


if __name__ == '__main__':

    # 执行计算
    flow_count()
