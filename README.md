end_gmail_py
=============


##This is a Python script to programmatically send templated emails to numerous recipients in a csv file


###Edit the following configuration lines


<pre><code>
username = 'gmail_username' #do not add @gmail.com!
password = 'gmail_password'
sender_name = 'Your Name'

csv_fname = 'emails.csv'
template_fname = 'email_template.txt'
email_subject = 'Email Subject'

</code></pre>


###Replace these fields as needed in the email template

<pre><code>
 msg = msg.replace('__RECIPIENT__', recipient)
 msg = msg.replace('__SENDER_NAME__', sender)
 msg = msg.replace('__COMPANY__', company)
</pre></code>
