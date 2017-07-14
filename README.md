# DataFrame2FFM
DataFrame数据格式转换成FFM格式  

**pandas_onehot函数** ：首先需要将数据转为onthot编码  

**data_convert2ffm函数**：其次将编码后的数据转为ffm格式数据  

The data format of LIBFFM is: <label> <field1>:<index1>:<value1> <field2>:<index2>:<value2> 
... field and index 是非负整数  

field：为同一onehot前的变量字段（即大的一个域）  
index：为编码后的字段的列序号  
value：为对一个的变量值
