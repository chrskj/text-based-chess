                ########################################################################################################
                if self.turn % 2:  # Hvis hvit sin tur
                    if self.B_king_pos in trussel_etter[3]:  # Hvis svart konge er truet etter hvit sitt trekk
                        while True:
                            farligeFiendeBrikker = []
                            print('SJAKK')

                            # Sjekker om kongen har en vei ut
                            for x in trussel_etter[0]:  # For mulige trekk til svart konge
                                if not self.sjakkbrett[x[0]][x[1]] and x not in trussel_etter[1]:  # Trekk som ikke er truet
                                    print('Det er visst en vei ut')
                                    return 'WP'

                            # Sjekker hvilke brikker som truer kongen
                            for kolonne in self.sjakkbrett:
                                for rute in kolonne:
                                    if rute and rute.color == 'W':
                                        if rute.is_valid_movement(self.B_king_pos[0], self.B_king_pos[1], self.sjakkbrett, self.history, trussel_før):
                                            farligeFiendeBrikker.append(rute)

                            # Hvis kongen står i sjakk av flere brikker
                            if len(farligeFiendeBrikker) > 2:
                                print('MATT')
                                return 'GG'

                            # Sjekker om noen brikker kan ta fiendebrikken som sjakker
                            for kolonne in self.sjakkbrett:
                                for rute in kolonne:
                                    if rute and rute.color == 'B':
                                        if rute.is_valid_movement(farligeFiendeBrikker[0].x, farligeFiendeBrikker[0].y, self.sjakkbrett, self.history, trussel_før):
                                            print('Backup is on the way')
                                            return 'WP'

                            # Finner rutene mellom kongen og den fiendtlige brikken som sjakker
                            x, y = farligeFiendeBrikker[0].x, farligeFiendeBrikker[0].y
                            a, b = self.B_king_pos[0], self.B_king_pos[1]
                            mulige_block_ruter = []
                            if x == a:  # Loddrett
                                mini = min(b, y)
                                maxi = max(b, y)
                                for i in range(1, maxi - mini):
                                    mulige_block_ruter.append([x, mini + i])
                            elif y == b:  # Vannrett
                                mini = min(a, x)
                                maxi = max(a, x)
                                for i in range(1, maxi - mini):
                                    mulige_block_ruter.append([mini+ i, y])
                            else:  # Diagonalt
                                xamax = max(x,a)
                                xamin = min(x,a)
                                ybmax = max(y,b)
                                ybmin = min(y,b)
                                for i in range(1, xamax-xamin):
                                    for j in range(1, ybmax-ybmin):
                                        mulige_block_ruter.append([xamin+i, ybmin+j])

                            # Sjekker om noen vennlige brikker kan blokkere sjakken
                            for kolonne in self.sjakkbrett:
                                for rute in kolonne:
                                    if rute and rute.color == 'B':
                                        for mulig_rute in mulige_block_ruter:
                                            if rute.is_valid_movement(mulig_rute[0], mulig_rute[1], self.sjakkbrett, self.history, trussel_før):
                                                print('Thank the heavens we are saved!')
                                                return 'WP'
                            print('MATT')
                            return 'GG'
                else:
                    if self.W_king_pos in trussel_etter[1]:  # Hvis hvit konge er truet etter svart sitt trekk
                        while True:
                            farligeFiendeBrikker = []
                            print('SJAKK')

                            # Sjekker om kongen har en vei ut
                            for x in trussel_etter[2]:  # For mulige trekk til hvit konge
                                if not self.sjakkbrett[x[0]][x[1]] and x not in trussel_etter[1]:  # Trekk som ikke er truet
                                    print('Det er visst en vei ut')
                                    return 'WP'

                            # Sjekker hvilke brikker som truer kongen
                            for kolonne in self.sjakkbrett:
                                for rute in kolonne:
                                    if rute and rute.color == 'B': #C
                                        if rute.is_valid_movement(self.W_king_pos[0], self.W_king_pos[1], self.sjakkbrett, self.history, trussel_før):
                                            farligeFiendeBrikker.append(rute)

                            # Hvis kongen står i sjakk av flere brikker
                            if len(farligeFiendeBrikker) > 2:
                                print('MATT')
                                return 'GG'

                            # Sjekker om noen brikker kan ta fiendebrikken som sjakker
                            for kolonne in self.sjakkbrett:
                                for rute in kolonne:
                                    if rute and rute.color == 'W': #C
                                        if rute.is_valid_movement(farligeFiendeBrikker[0].x, farligeFiendeBrikker[0].y, self.sjakkbrett, self.history, trussel_før):
                                            print('Backup is on the way')
                                            return 'WP'

                            # Finner rutene mellom kongen og den fiendtlige brikken som sjakker
                            x, y = farligeFiendeBrikker[0].x, farligeFiendeBrikker[0].y
                            a, b = self.W_king_pos[0], self.W_king_pos[1] #C
                            mulige_block_ruter = []
                            if x == a:  # Loddrett
                                mini = min(b, y)
                                maxi = max(b, y)
                                for i in range(1, maxi - mini):
                                    mulige_block_ruter.append([x, mini + i])
                            elif y == b:  # Vannrett
                                mini = min(a, x)
                                maxi = max(a, x)
                                for i in range(1, maxi - mini):
                                    mulige_block_ruter.append([mini+ i, y])
                            else:  # Diagonalt
                                xamax = max(x,a)
                                xamin = min(x,a)
                                ybmax = max(y,b)
                                ybmin = min(y,b)
                                for i in range(1, xamax-xamin):
                                    for j in range(1, ybmax-ybmin):
                                        mulige_block_ruter.append([xamin+i, ybmin+j])

                            # Sjekker om noen vennlige brikker kan blokkere sjakken
                            for kolonne in self.sjakkbrett:
                                for rute in kolonne:
                                    if rute and rute.color == 'W': #C
                                        for mulig_rute in mulige_block_ruter:
                                            if rute.is_valid_movement(mulig_rute[0], mulig_rute[1], self.sjakkbrett, self.history, trussel_før):
                                                print('Thank the heavens we are saved!')
                                                return 'WP'
                            print('MATT')
                            return 'GG'
                ########################################################################################################
