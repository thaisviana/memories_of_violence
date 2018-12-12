import rows
import uuid
from datetime import date
from occurrence.models import Occurrence, Asset


def extract():
    path = 'BANCO DE DADOS __ MAPA DA VIOLÊNCIA - BANCO DE DADOS.csv'
    data = rows.import_from_csv(path)
    for line in data:
        occurrence_date = line.data if line.data else None
        start = line.inicio if line.inicio else None
        finish = line.fim if line.fim else None
        try:
            if occurrence_date:
                occurrence_date_list = occurrence_date.split('/')
                if len(occurrence_date_list) == 2:
                    occurrence_date = date(int(occurrence_date_list[1].replace('.', '')),
                                           int(occurrence_date_list[0]),
                                           1)
                elif len(occurrence_date_list) == 3:
                    occurrence_date = date(int(occurrence_date_list[2].replace('.', '')),
                                           int(occurrence_date_list[1]),
                                           int(occurrence_date_list[0]))
                else:
                    occurrence_date = None
            if start:
                occurrence_date_list = start.split('/')
                if len(occurrence_date_list) == 2:
                    start = date(int(occurrence_date_list[1].replace('.', '')),
                                           int(occurrence_date_list[0]),
                                           1)
                elif len(occurrence_date_list) == 3:
                    start = date(int(occurrence_date_list[2].replace('.', '')),
                                           int(occurrence_date_list[1]),
                                           int(occurrence_date_list[0]))
                else:
                    start = None
            if finish:
                occurrence_date_list = finish.split('/')
                if len(occurrence_date_list) == 2:
                    finish = date(int(occurrence_date_list[1].replace('.', '')),
                                int(occurrence_date_list[0]),
                                1)
                elif len(occurrence_date_list) == 3:
                    finish = date(int(occurrence_date_list[2].replace('.', '')),
                                int(occurrence_date_list[1]),
                                int(occurrence_date_list[0]))
                else:
                    finish = None
        except:
            print(line.data)
            occurrence_date = None
            start = None
            finish = None
            pass
        o = Occurrence(
            description=line.nome,
            category=line.categoria.strip() if line.categoria else "Indefinido",
            preciseDate=occurrence_date,
            startDate=start,
            finishDate=finish,
            report=line.reportagem_url if line.reportagem_url else None,
            manifestations=line.atos_e_manifestacoes if line.atos_e_manifestacoes else None,
            stories=line.fichas_narrativas if line.fichas_narrativas else None
        )
        o.save()
        if line.foto_externa_url and 'http' in line.foto_externa_url:
            a = Asset(url=line.foto_externa_url, occurrence=o, type='IM', hashId=uuid.uuid4().__str__())
            a.save()
        if line.foto_interna_nome_do_arquivo_salvo_no_drive \
                and 'http' in line.foto_interna_nome_do_arquivo_salvo_no_drive:
            a = Asset(url=line.foto_interna_nome_do_arquivo_salvo_no_drive,
                      occurrence=o, type='IM', hashId=uuid.uuid4().__str__())
            a.save()
        if line.video_url and 'http' in line.video_url:
            a = Asset(url=line.video_url,
                      occurrence=o, type='VI', hashId=uuid.uuid4().__str__())
            a.save()
