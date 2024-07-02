import sys
import pandas as pd

def filter_csv(csv_file, filter_expr, page_size=50, page_number=1):
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        sys.exit(1)
    
    filtered_df = df.query(filter_expr)
    
    # Paginate results
    start_idx = (page_number - 1) * page_size
    end_idx = start_idx + page_size
    paginated_results = filtered_df.iloc[start_idx:end_idx]
    
    return paginated_results

if __name__ == "__main__":

    filter_expr = "(Age >= 30) and (City == 'New York' or City == 'San Francisco')"
    page_size = 3
    page_number = 1
    
    results = filter_csv('sample_data.csv', filter_expr, page_size, page_number)
    
    print(results)
