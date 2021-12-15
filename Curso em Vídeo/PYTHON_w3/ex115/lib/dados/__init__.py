def arqExiste(path, arq):
    try:
        a = open((path+arq), 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arqCriar(path, arq):
    try:
        a = open((path+arq), 'wt+')
    except:
        return False
    else:
        return True
    finally:
        a.close()


def arqLer(path, arq):
    try:
        a = open((path+arq), 'rt')
    except:
        return False
    else:
        return a.readlines()
    finally:
        a.close()


def arqCadastro(path, arq, nome='desconhecido', idade=0):
    try:
        a = open((path+arq), 'at')
    except:
        return False
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            return False
        else:
            return True
    finally:
        a.close()
