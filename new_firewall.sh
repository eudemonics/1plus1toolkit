#!/bin/bash
# AUTHOR: vvn <vvn@notworth.it>
# CUSTOM FIREWALL FOR ANDROID - MUST RUN AS ROOT

echo "STARTING CUSTOM FIREWALL SCRIPT BY VVN..."
echo "***script needs to be run as root***"
sleep 3

#clear all rules
iptables -F

#set default policy
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

#allowing and rejecting port 80 http, 443 https traffic by changing jumper option from ACCEPT to DROP
#HTTP - 80
iptables -A INPUT -i eth0 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT
#HTTPS - 443
iptables -A INPUT -i eth0 -p tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 443 -m state --state ESTABLISHED -j ACCEPT

#block specific ip address
ip_block="192.168.43.1"
iptables -A INPUT -s "$ip_block" -j ACCEPT

#accept specific ip address
ip_accept="192.168.43.1"
iptables -A INPUT -s "$ip_accept" -j ACCEPT
iptables -A OUTPUT -s "$ip_accept" -j ACCEPT

#Blocking ICMP echo packets from outside
iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
iptables -A OUTPUT -p icmp --icmp-type echo-reply -j DROP


#Postfix traffic rules
iptables -A INPUT -i eth0 -p tcp --dport 25 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 25 -m state --state ESTABLISHED -j ACCEPT

#Imap traffic rules
iptables -A INPUT -i eth0 -p tcp --dport 143 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 143 -m state --state ESTABLISHED -j ACCEPT

#Pop3 traffic rules
iptables -A INPUT -i eth0 -p tcp --dport 110 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 110 -m state --state ESTABLISHED -j ACCEPT

#FTP traffic rules

#allow incoming FTP
iptables -A INPUT -i eth0 -p tcp --dport 21 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 21 -m state --state ESTABLISHED -j ACCEPT
# SFTP
iptables -A INPUT -i eth0 -p tcp --dport 2222 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 2222 -m state --state ESTABLISHED -j ACCEPT

#allow outgoing FTP
iptables -A OUTPUT -o eth0 -p tcp --dport 21 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -i eth0 -p tcp --sport 21 -m state --state ESTABLISHED -j ACCEPT
# SFTP
iptables -A OUTPUT -o eth0 -p tcp --dport 2222 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -i eth0 -p tcp --sport 2222 -m state --state ESTABLISHED -j ACCEPT

#Allowing and rejecting port 22 ssh traffic by just changing jumper option from ACCEPT to DROP

#allow incoming ssh traffic
iptables -A INPUT -i eth0 -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

#allow outgoing ssh traffic
iptables -A OUTPUT -o eth0 -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -i eth0 -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

#allow drozer incoming
iptables -A INPUT -i eth0 -p tcp --dport 31415 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 31415 -m state --state ESTABLISHED -j ACCEPT

#allow drozer outgoing
iptables -A OUTPUT -o eth0 -p tcp --dport 31415 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -i eth0 -p tcp --sport 31415 -m state --state ESTABLISHED -j ACCEPT

#allow privoxy incoming
iptables -A INPUT -i eth0 -p tcp --dport 8118 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 8118 -m state --state ESTABLISHED -j ACCEPT

#allow privoxy outgoing
iptables -A OUTPUT -o eth0 -p tcp --dport 8118 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -i eth0 -p tcp --sport 8118 -m state --state ESTABLISHED -j ACCEPT

#allow tor incoming
iptables -A INPUT -i eth0 -p tcp --dport 9050 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 9050 -m state --state ESTABLISHED -j ACCEPT

#allow tor outgoing
iptables -A OUTPUT -o eth0 -p tcp --dport 9050 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -i eth0 -p tcp --sport 9050 -m state --state ESTABLISHED -j ACCEPT

#Denial-of-service attack prevention rule
#17/minute means it will allow 17 connections per minute and when it gets whole of those connections then total 40 connections will enforced by burst limit.
iptables -A INPUT -p tcp --dport 80 -m limit --limit 17/minute --limit-burst 40 -j ACCEPT

#Listing rules
iptables -L

