from django.shortcuts import render
import mysql.connector as sql

def serchaction(request):
    if request.method == "POST":
        
        # Get the search query from the form
        q = request.POST.get('q', '')
        # Perform the search using the query 'q' and fetch the results from your database
        m=sql.connect(host="localhost",user="root",password="your password here",database='your databse name',auth_plugin="mysql_native_password")
        cursor=m.cursor()
        l="selcet * fro your table_name" 
        cursor.execute(l)
        results=cursor.fetchall()
        if results!=():
            results=results
        else:
            results=''
        return render(request, 'result.html', {'results': results})
    else:
        # Handle GET request or other cases
        return render(request, 'welcome.html')
