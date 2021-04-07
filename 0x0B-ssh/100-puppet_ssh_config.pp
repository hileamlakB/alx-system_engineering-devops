# Addes some configration to the ssh_config file

exec { 'ssh_config':
  command => 'echo -e "\n"'

}
