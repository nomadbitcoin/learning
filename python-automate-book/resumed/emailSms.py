*******************************************************************************
*********************** conectando e enviando emails **************************
*******************************************************************************

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)	#configura a conexao com o servidor de email e porta
smtpObj.ehlo()	#confirma conexao com o servidor de email	-se retornar 250 significa que conectou-
smtpObj.starttls()	#inicia protocolo criptografia tls (porta 587)	-se retornar 220 servidor esta pronto-
smtpObj.login('yaaanhue@gmail.com',password)	#faz login no servidor de email -se retornar 235 conectou-
smtpObj.sendmail('yaaanhue@gmail.com','machadonycolas3@gmail.com',text)	#envia email, pode colocar inumeros destinatarios -tem que comecar com Subject: \n
smtpObj.quit()

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)	#configura a conexao com o servidor de email e porta
smtpObj.ehlo()	#confirma conexao com o servidor de email	-se retornar 250 significa que conectou-
smtpObj.starttls()	#inicia protocolo criptografia tls (porta 587)	-se retornar 220 servidor esta pronto-
passwd = input()
smtpObj.login('yaaanhue@gmail.com',passwd)	#faz login no servidor de email -se retornar 235 conectou-

inp = input('Enter password: ')
text = 'Subject: So long.\n'+inp

smtpObj.sendmail('yaaanhue@gmail.com','machadonycolas3@gmail.com',text)	#envia email, pode colocar inumeros destinatarios -tem que comecar com Subject: \n

s = smtpObj.quit()
if s[0] == 221:
	print('Done')



*******************************************************************************
**************** acessando inbox e lendo emails de remetente ******************
*******************************************************************************

import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com',use_uid=True)
passwd = input('Enter password: ')
imapObj.login('yaaanhue@gmail.com',passwd)
select_info = imapObj.select_folder('INBOX')
print('%d messages in INBOX' % select_info[b'EXISTS'])
messages = imapObj.search(['FROM','no-reply@blockchain.info'])
print('%d messages from Searched Mail' % len(messages))
for msgid, data in imapObj.fetch(messages, ['ENVELOPE']).items():
	envelope = data[b'ENVELOPE']
	print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))