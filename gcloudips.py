import re
import logging
import subprocess

def get_netblock_ips_cidr(netblock_id):
    '''Run the nslookup comamnd on the given netlock, and yield all of the ip
     address cidr addresses'''
    netblock = "_cloud-netblocks%d.googleusercontent.com"%netblock_id
    logging.info("Running Netblock %s", netblock)
    CMD = 'nslookup -q=TXT %s 8.8.8.8'%netblock
    p = subprocess.Popen(CMD, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()
    output_text = out.decode('utf-8')
    re_ips = re.compile(r"ip4:(?P<ipcidr>[\.\d]+/\d+)")
    num = 0
    for m in re_ips.finditer(output_text):
        yield m.group('ipcidr')
        num += 1
    logging.info("Netblock %s: Found %d IPs", netblock, num)

def get_all_ip_cidrs(max_net_block_ranges = 10):
    logging.getLogger().setLevel(logging.INFO)
    '''Run it across '''
    netblock_id = 0
    for netblock_id in range(1, max_net_block_ranges):
        for cidr in get_netblock_ips_cidr(netblock_id):
            yield cidr
    logging.info("Finished after %d netblocks"%netblock_id)

def main():
    ip_list=list(get_all_ip_cidrs())
    list_size=len(ip_list)

    logging.info("Found %d ip addresses.", list_size)
    logging.info("Writing to file gcloudips.out")
    f = open("gcloudips.out", "w")
    for ip in ip_list:
        f.write('%s\n' % ip)
    f.close()
    

if __name__ == "__main__":
    main()