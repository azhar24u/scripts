

if __name_=='__main__':
        start_run_time=time.time()
        res_process=1
        num_params=len(sys.argv)
        log_folder_name=os.environ['UNXLOG']
        if num_params == 3 :
                log_file_name=Constants.ARB_DQ_TECH_LOG + datetime.now().strftime(Constants_ARB_DQ_LOG_TMST_FTM) + Constants.ARB_DQ_LOG_EXT
                arg_param={ 
                        Constants.ARB_CONF_FILE : sys.argv[1],
                        Constants.ARB_DQCSV_NAME : sys.argv[2]
                        Constants.ARB_PROCESS_NAME : Constants.ARB_DQ_CSV_PROCESS_ID,
                        Constants.ARB_LOG_DIR : log_folder_name,
                        Constants.ARB_LOG_FILE : log_file_name,
                        Constants.ARB_DEBUG_MODE : Constants.ARB_DEBUG_MODE_ACTIVATED,
                        Constants.ARB_CONSOLE_PRINT : Constants.ARB_CONSOLE_PRINT_ACTIVATED,
                        Constants.ARB_DQ_DATETIME : datetime.strptime(end_date, Constants.ARB_DQ_TMSTMP_FMT)
