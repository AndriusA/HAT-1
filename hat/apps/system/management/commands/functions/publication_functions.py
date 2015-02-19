# Django
from django.template.defaultfilters import slugify

# Essen
from essen.apps.publications.models import (PublicationResearchArea,
                                            PublicationApplication)


def publication_research(row, publication, areas):
    for area in areas:
        if row[area]:
            try:
                research_area = PublicationResearchArea.objects.get(
                    title=row[area]
                )
                publication.research_areas.add(
                    research_area
                )
                print "Found research area"

            except Exception:
                new_research_area = PublicationResearchArea(
                    title=row[area],
                    url_title=slugify(row[area])
                )

                new_research_area.save()

                publication.research_areas.add(
                    new_research_area
                )

                print "Added research area"


def publication_application(row, publication, applications):
    for application in applications:
        if row[application] != "" and row[application] != "Not Known":

            try:
                publication_application = PublicationApplication.objects.get(
                    title=row[application]
                )

                publication.publication_applications.add(
                    publication_application
                )

                print "Found application"

            except Exception:

                new_application = PublicationApplication(
                    title=row[application],
                    url_title=slugify(row[application])
                )

                new_application.save()

                publication.publication_applications.add(
                    new_application
                )

                print "Added application"
