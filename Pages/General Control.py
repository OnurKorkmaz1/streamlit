import streamlit as st
import plotly.graph_objects as go
import pandas as pd



# Streamlit uygulama başlatma
st.title("Revit Model Health Check")
#st.markdown("Bu örnekte Revit modelinin sağlık kontrolü sonuçlarını Gauge (ölçek) grafiği kullanarak gösteriyoruz.")

# Create Radio Buttons
options = st.radio(label = 'CONTROL', options = ['Family Name','Material Name','Assembly Code','Room Status'])
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

def gauge_chart(value, title):
    if value <= 30:
        color = "red"
    elif value <= 70:
        color = "yellow"
    else:
        color = "green"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': 'white'},
                {'range': [30, 70], 'color': 'white'},
                {'range': [70, 100], 'color': 'white'}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': 80
            }
        }
    ))

    return fig

# Rastgele bir değer oluşturma
P_familyname = 25
P_materialname = 50
P_assemblycode = 60
P_RoomStatus = 88
# Gauge grafiğini oluşturma ve gösterme
#fig = gauge_chart(revit_puan, "Revit Model Puanı")
#st.plotly_chart(fig)


def familyname(dataframe):

    st.markdown(""" <style> .font {
        font-size:30px ; font-family: 'Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)

    st.markdown('<p class="font">RESULT</p>', unsafe_allow_html=True)
  
    fig = gauge_chart(P_familyname, "Model Health")
    st.plotly_chart(fig)

def materialname(dataframe):

    st.markdown(""" <style> .font {
        font-size:30px ; font-family: 'Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)

    st.markdown('<p class="font">RESULT</p>', unsafe_allow_html=True)

    fig = gauge_chart(P_materialname, "Model Health")
    st.plotly_chart(fig)

def assemblycode(dataframe):

    st.markdown(""" <style> .font {
        font-size:30px ; font-family: 'Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)

    st.markdown('<p class="font">RESULT</p>', unsafe_allow_html=True)

    fig = gauge_chart(P_assemblycode, "Model Health")
    st.plotly_chart(fig)

def RoomStatus(dataframe):

    st.markdown(""" <style> .font {
        font-size:30px ; font-family: 'Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)

    st.markdown('<p class="font">RESULT</p>', unsafe_allow_html=True)

    fig = gauge_chart(P_RoomStatus, "Model Health")
    st.plotly_chart(fig)



if options == "Family Name":
    familyname(P_familyname)
elif options == "Material Name":
    materialname(P_materialname)
elif options == "Assembly Code":
    assemblycode(P_assemblycode)
elif options == "Room Status":
    RoomStatus(P_RoomStatus)

df = pd.read_excel("ModelData.xlsx") 
st.write(df)
