#Преобразование вывода show cdp neighbors, взятого из файла в словарь с записями для каждого соединения вида {(локальное_устройство, локальный_порт):(удалённое устройство, удалённый порт)}
#Converting show cdp neighbors output into dictionary with records for each neighbor looking like {(local_device, local_port):(remote_device,remote_port)}

cdp_nei_file_name = 'sh_cdp_n_sw1.txt'

def parse_cdp_nei(cdp_nei_output):
	device_name = cdp_nei_output.split('>')[0].replace('\n','')
	# Разбить вывод show cdp nei на строки
	neighbors = cdp_nei_output.split('Port ID')[1].split('\n')
	
	connections_dict = {}
	
	# Удалить пустые элементы 
	while '' in neighbors:
		neighbors.remove('')

	#Для каждой линии сначала и с конца отщипываются значения устройств и портов, формируется строка в словаре
	for neighbor_line in neighbors:
		connections_dict.update({(device_name, neighbor_line.split()[1]+neighbor_line.split()[2]):(neighbor_line.split()[0],neighbor_line.split()[-2]+neighbor_line.split()[-1])}) 
		
	return connections_dict

cdp_nei_file = open(cdp_nei_file_name, 'r')
cdp_nei_output_string = cdp_nei_file.read()

print(parse_cdp_nei(cdp_nei_output_string))
