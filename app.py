import streamlit.components.v1 as components

from app.ui import run_ui

clarity_code = """
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/" + i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "wwbfes9wuy");
</script>
"""

components.html(clarity_code, height=0)

run_ui()