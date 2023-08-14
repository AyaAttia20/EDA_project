import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px




st.write("""
         Automated Exploratory Data Analysis : (EDA )
         
         """)



Select = st.sidebar.selectbox("Select Option", ('Exploratory Data Analysis ','plots','show Code'))
if Select=='Exploratory Data Analysis ':

    data=st.file_uploader('Upload File',type=['csv','txt','xlsx'])

    if data is not None:
        df=pd.read_csv(data)
        # st.dataframe(df.head())
        if st.button('show data'):
            st.dataframe(df.sample(5))

        
        if st.button('Data Analysis'):
        
            st.title('**Data Details**')  
            st.write(df.shape)
            
            st.title('**Data  columns inforamation**')  
            st.write(df.columns.to_list())
        
            
            
            
            st.title('**Data sammary**')  
            st.write(df.describe())
            


            st.title('**Data Cleaning**')
            st.write(df.isna().sum())
            st.write(df.duplicated().sum())
       
        

            st.title('**value count of variables**')
            for i in df.columns:
                st.title(i)
                st.write(df[i].value_counts())
        

elif Select=='plots':
       data=st.file_uploader('Upload File',type=['csv','txt','xlsx'])


       if data is not None:
           data.seek(0)
           df=pd.read_csv(data,low_memory=False)
        #    st.dataframe(df.head())
           if st.button('show data'):
            st.dataframe(df.sample(5))

           st.title('**Data Visulization**')
    
           col=df.columns
           type_of_plot=st.radio('select plot type ',options=['line','hist','bar'])
           selected_colum = st.multiselect("Select Columns To Plot",col)
           if st.button('plotting Data'):
                st.success("plotting Data  {} for {}".format(type_of_plot,selected_colum))
                if type_of_plot=='line':
                    st.subheader('Line plotting')
                    fig=plt.figure(figsize=(15,8))
                    plt.plot(selected_colum)
                    st.pyplot(fig)
                elif type_of_plot=='hist':  
                    st.subheader('Histgram plotting')
                    fig=plt.figure(figsize=(15,8))
                    sns.histplot(x=selected_colum,hue=selected_colum)
                    st.pyplot(fig)  
                elif type_of_plot=='bar':   
                    st.subheader('Bar plotting')
                    fig=px.bar(data_frame=df,x=selected_colum)
                    st.plotly_chart(fig)
 




elif Select=='show Code':  
    st.subheader('code of APP')     
    code="""
import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px




st.write(""Automated Exploratory Data Analysis : (EDA )
    
    
     "")



Select = st.sidebar.selectbox("Select Option", ('Exploratory Data Analysis ','plots','show Code'))
if Select=='Exploratory Data Analysis ':

    data=st.file_uploader('Upload File',type=['csv','txt','xlsx'])

    if data is not None:
        df=pd.read_csv(data)
        # st.dataframe(df.head())
        if st.button('show data'):
            st.dataframe(df.sample(5))

        
        if st.button('Data Analysis'):
        
            st.title('**Data Details**')  
            st.write(df.shape)
            
            st.title('**Data  columns inforamation**')  
            st.write(df.columns.to_list())
        
            
            
            
            st.title('**Data sammary**')  
            st.write(df.describe())
            


            st.title('**Data Cleaning**')
            st.write(df.isna().sum())
            st.write(df.duplicated().sum())
       
        

            st.title('**value count of variables**')
            for i in df.columns:
                st.title(i)
                st.write(df[i].value_counts())
        

elif Select=='plots':
       data=st.file_uploader('Upload File',type=['csv','txt','xlsx'])


       if data is not None:
           data.seek(0)
           df=pd.read_csv(data,low_memory=False)
        #    st.dataframe(df.head())
           if st.button('show data'):
            st.dataframe(df.sample(5))

           st.title('**Data Visulization**')
    
           col=df.columns
           type_of_plot=st.radio('select plot type ',options=['bar','line','hist'])
           selected_colum = st.multiselect("Select Columns To Plot",col)
           if st.button('plotting Data'):
                st.success("plotting Data  {} for {}".format(type_of_plot,selected_colum))
                if type_of_plot=='line':
                    st.subheader('Line plotting')
                    fig=plt.figure(figsize=(15,8))
                    plt.plot(selected_colum)
                    st.pyplot(fig)
                elif type_of_plot=='hist':  
                    st.subheader('Histgram plotting')
                    fig=plt.figure(figsize=(15,8))
                    sns.histplot(x=selected_colum,hue=selected_colum)
                    st.pyplot(fig)  
                elif type_of_plot=='bar':   
                    st.subheader('Bar plotting')
                    fig=px.bar(data_frame=df,x=selected_colum)
                    st.plotly_chart(fig)
 



    """



    st.code(code, language='python')
    st.write("Created By: Aya Attia")


           

            
               

        
            






               

    



                


               

                
                     

              

        
                # if type_of_plot == 'bar':
                #     st.write('This is bar plotting ')
                #     ploted_col = df[selected_colum]
                #     st.bar_chart(ploted_col)

                # elif type_of_plot == 'line':
                #     st.write('This is line plotting ')
                #     ploted_col = df[selected_colum]
                #     st.line_chart(ploted_col)

                # elif type_of_plot == 'hist':
                #     st.write('This is histogram plotting ')
                #     ploted_col = df[selected_colum]
                #     st.pyplot(ploted_col)

                
                


                



    
