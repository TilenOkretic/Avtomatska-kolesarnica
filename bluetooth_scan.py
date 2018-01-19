import bluetooth

def main(args):
	while True:
		nearby_devices = bluetooth.discover_devices(lookup_names=True)
		print("found %d devices" % len(nearby_devices))

		for addr, name in nearby_devices:
			print("  %s - %s" % (addr, name))
		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
