import multiprocessing
import pandas as pd
from clever_prompt_detector import get_result
import multiprocessing

def process_row(row, progress_counter, total_rows, ans):
    """打印一行CSV数据并更新进度。"""
    process_id = multiprocessing.current_process().name
    with multiprocessing.Lock():
        progress_counter.value += 1
        print(f"Progress: {(progress_counter.value/total_rows)*100:.2f}% index: {row['index']}  Ans: ", end='')
        result = get_result.query(row['query'])
        ans.append([row['index'],row['query'],result[1],result[0]])
        if result[1]:
            print(f"TRUE  {process_id}")
        else:
            print(f"FALSE {process_id}")

def process_csv_file(csv_path, num_processes=50):
    """使用多进程读取并打印CSV文件，并显示进度。

    Args:
        csv_path: CSV文件的路径。
        num_processes: 要使用的进程数。
    """
    df = pd.read_csv(csv_path)
    df['index'] = df.index
    total_rows = df.index.stop
    print(f"Total rows: {total_rows}")
    # 使用 Manager.list() 来创建一个共享的列表，用于跟踪已处理的行
    manager = multiprocessing.Manager()
    processed_rows = manager.list()
    global ans
    ans = manager.list()
    progress_counter = manager.Value('i', 0)  # 使用共享整数来跟踪进度
    with multiprocessing.Pool(processes=num_processes) as pool:
        for i in range(df.index.stop):
            # 检查该行是否已被处理
            row = df.loc[i,:]
            row_tuple = tuple(row)
            if row_tuple not in processed_rows:
                # 使用 apply_async 异步提交任务
                pool.apply_async(process_row, (row, progress_counter, total_rows, ans))
                processed_rows.append(row_tuple)

        # 关闭进程池，不再接受新的任务
        pool.close()
        # 等待所有进程完成
        pool.join()
        print("\nProcessing complete!")

if __name__ == '__main__':
    csv_filename = "./new_data.csv"  # 替换为你的CSV文件名
    process_csv_file(csv_filename)
    df = pd.DataFrame(ans[:], columns=None)
    df.to_csv("result.csv",index=False,encoding='utf-8',header=None)