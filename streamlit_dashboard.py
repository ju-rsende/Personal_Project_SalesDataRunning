import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configure Streamlit page
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API Base URL
API_BASE = "http://localhost:8000/api"

@st.cache_data(ttl=60)
def fetch_data(endpoint):
    """Fetch data from Django API"""
    try:
        response = requests.get(f"{API_BASE}/{endpoint}/")
        return response.json()
    except:
        return {}

def main():
    st.title("📊 Sales Analytics Dashboard")
    st.markdown("---")
    
    # Fetch all data
    dashboard_data = fetch_data("dashboard")
    suppliers_data = fetch_data("suppliers")
    clients_data = fetch_data("clients")
    products_data = fetch_data("products")
    
    if not dashboard_data:
        st.error("❌ Cannot connect to Django API. Make sure the server is running on port 8000.")
        return
    
    # Key Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Records", 
            dashboard_data.get('total_records', 0),
            delta=None
        )
    
    with col2:
        revenue = dashboard_data.get('total_revenue', 0)
        st.metric(
            "Total Revenue", 
            f"${revenue:,.2f}",
            delta=None
        )
    
    with col3:
        st.metric(
            "Top Countries", 
            len(clients_data),
            delta=None
        )
    
    with col4:
        st.metric(
            "Product Types", 
            len(products_data),
            delta=None
        )
    
    st.markdown("---")
    
    # Charts Row 1
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏭 Top Suppliers by Cost")
        if suppliers_data:
            df_suppliers = pd.DataFrame(list(suppliers_data.items()), columns=['Country', 'Total Cost'])
            fig = px.bar(
                df_suppliers.head(10), 
                x='Country', 
                y='Total Cost',
                color='Total Cost',
                color_continuous_scale='Reds'
            )
            fig.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🌍 Top Clients by Revenue")
        if clients_data:
            df_clients = pd.DataFrame(list(clients_data.items()), columns=['Country', 'Total Revenue'])
            fig = px.bar(
                df_clients.head(10), 
                x='Country', 
                y='Total Revenue',
                color='Total Revenue',
                color_continuous_scale='Blues'
            )
            fig.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
    
    # Charts Row 2
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📦 Product Performance")
        if products_data:
            df_products = pd.DataFrame(list(products_data.items()), columns=['Product', 'Units Sold'])
            fig = px.pie(
                df_products, 
                values='Units Sold', 
                names='Product',
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💰 Revenue vs Cost Analysis")
        if suppliers_data and clients_data:
            # Create comparison chart
            countries = list(set(suppliers_data.keys()) & set(clients_data.keys()))[:8]
            
            fig = go.Figure()
            fig.add_trace(go.Bar(
                name='Revenue',
                x=countries,
                y=[clients_data.get(c, 0) for c in countries],
                marker_color='lightblue'
            ))
            fig.add_trace(go.Bar(
                name='Cost',
                x=countries,
                y=[suppliers_data.get(c, 0) for c in countries],
                marker_color='lightcoral'
            ))
            
            fig.update_layout(
                barmode='group',
                height=400,
                title="Revenue vs Cost by Country"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Data Tables
    st.markdown("---")
    st.subheader("📋 Detailed Data")
    
    tab1, tab2, tab3 = st.tabs(["Suppliers", "Clients", "Products"])
    
    with tab1:
        if suppliers_data:
            df = pd.DataFrame(list(suppliers_data.items()), columns=['Country', 'Total Cost'])
            df['Total Cost'] = df['Total Cost'].apply(lambda x: f"${x:,.2f}")
            st.dataframe(df, use_container_width=True)
    
    with tab2:
        if clients_data:
            df = pd.DataFrame(list(clients_data.items()), columns=['Country', 'Total Revenue'])
            df['Total Revenue'] = df['Total Revenue'].apply(lambda x: f"${x:,.2f}")
            st.dataframe(df, use_container_width=True)
    
    with tab3:
        if products_data:
            df = pd.DataFrame(list(products_data.items()), columns=['Product', 'Units Sold'])
            df['Units Sold'] = df['Units Sold'].apply(lambda x: f"{x:,}")
            st.dataframe(df, use_container_width=True)

# Sidebar
with st.sidebar:
    st.header("🔧 Controls")
    
    if st.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📊 Dashboard Features")
    st.markdown("- Real-time data from Django API")
    st.markdown("- Interactive charts with Plotly")
    st.markdown("- Responsive design")
    st.markdown("- Auto-refresh capability")
    
    st.markdown("---")
    st.markdown("### 🔗 Quick Links")
    st.markdown("[Django Admin](http://localhost:8000/admin)")
    st.markdown("[API Endpoints](http://localhost:8000/api/dashboard)")

if __name__ == "__main__":
    main()