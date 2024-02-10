# Streamlit
import streamlit as st
import streamlit.components.v1 as stc

# Import EDA
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel

# Load dataset
def load_data(data):
    df = pd.read_csv("data")
    return df
# Fxn
# Vectorize + Cosine Similarity Matrix
def vectorize_text_to_cos_mat(data):
    count_vect = CountVectorizer()
    cvect_mat = count_vect.fit_transform(data)
    # Get the cosine
    cosine_sim_mat = cosine_similarity(cvect_mat)
    return cosine_sim_mat

# Rec Sys
@st.cache
def get_recommendation(title, cosine_sim_mat, df, num_of_rec=10):
    # Indices of the course 
    course_indices = pd.Series(df.index, index=df['course_title']).drop_duplicates()
    # Index of course
    idx = course_indices[title]

    # Look into the cosine matrix for that index
    sim_scores = list(enumerate(cosine_sim_mat[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    selected_course_indices = [i[0] for i in sim_scores[1:]] #return sim_scores[1:]
    selected_course_scores = [i[0] for i in sim_scores[1:]] #return sim_scores[1:]

    # Get the dataframe & title
    result_df = df.iloc[selected_course_indices]
    result_df['similarity_score'] = selected_course_scores
    final_recommended_course = result_df[['course_title','similarity_score','url','price','number_subscribers']]
    return final_recommended_course(num_of_rec)

# CSS style for search courses
RESULT_TEMP = """
<div style = "width:90%; height:100%; margin:1px; padding:5px; position:relaive; border-radius:5px; 
border-bottom:5px; box-shadow:0 0 15px 5px #ccc; background-color:#a8f0c6;
border-left: 5px solid #6c6c6c;">
<h4>{}</h4>
<p style="color:blue;"><span style="color:black;">📚 Score:</span>{}</p>
<p style="color:blue;"><span style="color:black;">🔗</span><a href="{}", target="_blank">Link</a></p>
<p style="color:blue;"><span style="color:black;">💰 Price:</span>{}</p>
<p style="color:blue;"><span style="color:black;">👨‍🎓👩‍🎓 Students:</span>{}</p>

</div>
"""
# Search for Course
@st.cache
def search_term_if_not_found(term,df):
    result_df = df[['course_title'].str.contains(term)]
    return result_df


def main():
    st.title("Course Recommendation App")

    menu = ["Home", "Recommend", "About"]
    choice = st.sidebar.selectbox("Menu",menu)

    df = load_data("E:\2023\01. Body of Knowledge\03.Courses\06. IBM Machine Learning Professional Certificate\06. ML Capstone\Week6\courses.csv")
    
    if choice == "Home":
        st.subheader("Home")
        st.dataframe(df.head(10))
        
    elif choice == "Recommend":
        st.subheader("Recommend Courses")
        cosine_sim_mat = vectorize_text_to_cos_mat(df["course_title"])
        search_term = st.text_input("Search")
        num_of_rec = st.sidebar.number_input("Number",4,30,7)
        if st.button("Recommend"):
            if search_term is not None:
                try:
                    results = get_recommendation(search_term, cosine_sim_mat,df, num_of_rec)#pass
                    with st.beta_expand_expander("Results as JSON"):
                        results_json = results.to_dict('index')
                        st.write(results_json)

                    for row in results.iterrows():
                        rec_title = row[1][0]
                        rec_score = row[1][1]
                        rec_url = row[1][2]
                        rec_price = row[1][3]
                        rec_num_subs = row[1][4]

                    #st.write("Title",rec_title)
                    stc.html(RESULT_TEMP.format(rec_title, rec_score, rec_url, rec_price, rec_num_subs), height = 350)

                except:
                    results = "Not Found"
                    st.warning(results)
                    st.info("Suggested options include")
                    result_df = search_term_if_not_found
                    st.dataframe(result_df)
                
                #st.write(results)
                

                # How to maximize your 
                
    else:
        st.subheader("About")
        st.text("Build with Streamlit")

if __name__== '__main__':
    main()    
