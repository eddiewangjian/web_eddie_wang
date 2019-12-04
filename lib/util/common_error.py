#coding=utf-8

class ErrorCode:
    # ------------------ 通用基础类型(自定义) ------------- 
    SUCCESS                 = 0         #处理成功 
    ERROR                   = 1         #处理错误 
    EXCEPTION               = 2         #处理异常 
    FAIL                    = 3         #业务失败 
    RUNNING                 = 4         #处理中 
    WAITING                 = 5         #待处理 
    PENDING                 = 6         #条件阻塞等待 
    STOPPED                 = 7         #中断停止 

    # --------------------- 框架错误类型 ------------------ 
    FRAMEWORK_ERROR         = 10001     #框架内部错误 
    FRAMEWORK_EXCEPTION     = 10002     #框架内部异常 

    # --------------------- 服务错误类型 ------------------ 
    SERVER_ERROR            = 20001     #服务内部错误 
    SERVER_EXCEPTION        = 20002     #服务内部异常 

    # --------------------- 网络错误类型 ------------------ 
    NETWORK_ERROR           = 30001     #网络异常 

    # --------------------- 客户端错误类型 ------------------ 
    CLIENT_ERROR            = 40001     #客户端内部错误 
    CLIENT_EXCEPTION        = 40002     #客户端内部异常 

    # ------------------ 业务错误类型(自定义) ------------- 
    BUSINESS_ERROR          = 50001     #业务逻辑错误 
    BUSINESS_EXCEPTION      = 50002     #业务异常 
    BUSINESS_FAIL           = 50003     #业务失败


