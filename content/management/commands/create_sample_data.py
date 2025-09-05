from django.core.management.base import BaseCommand
from content.models import Service, Project, TeamMember, CompanyInfo


class Command(BaseCommand):
    help = 'Create sample data for Tapara Dev website'

    def handle(self, *args, **options):
        # Create Company Info
        company_info = CompanyInfo.load()
        company_info.company_name = 'Tapara Dev'
        company_info.tagline = 'Desarrollo de aplicaciones web, móviles e integraciones'
        company_info.about_text = '''
        En Tapara Dev nos especializamos en el desarrollo de soluciones digitales innovadoras.
        Nuestro equipo combina experiencia técnica con creatividad para entregar productos
        de alta calidad que impulsan el crecimiento de nuestros clientes.
        '''
        company_info.mission = '''
        Nuestra misión es transformar ideas en soluciones digitales exitosas,
        utilizando las tecnologías más avanzadas y las mejores prácticas de desarrollo.
        '''
        company_info.vision = '''
        Ser reconocidos como el socio tecnológico preferido para empresas que buscan
        innovación y excelencia en sus proyectos digitales.
        '''
        company_info.email = 'contacto@tapara.dev'
        company_info.phone = '+58 424-1234567'
        company_info.address = 'Caracas, Venezuela'
        company_info.save()
        
        # Create Services
        services_data = [
            {
                'name': 'Desarrollo Web',
                'description': 'Creamos aplicaciones web modernas y responsivas utilizando las últimas tecnologías como Django, React, Vue.js y más. Desde sitios corporativos hasta aplicaciones web complejas.',
                'short_description': 'Aplicaciones web modernas y responsivas',
                'icon': 'fas fa-globe',
                'is_featured': True,
                'order': 1
            },
            {
                'name': 'Desarrollo Móvil',
                'description': 'Desarrollamos aplicaciones móviles nativas e híbridas para iOS y Android. Utilizamos React Native, Flutter y tecnologías nativas para crear experiencias móviles excepcionales.',
                'short_description': 'Apps móviles para iOS y Android',
                'icon': 'fas fa-mobile-alt',
                'is_featured': True,
                'order': 2
            },
            {
                'name': 'Integraciones',
                'description': 'Conectamos tus sistemas existentes con nuevas plataformas, APIs y servicios. Automatizamos procesos y mejoramos la eficiencia operacional de tu negocio.',
                'short_description': 'Conectamos sistemas y automatizamos procesos',
                'icon': 'fas fa-plug',
                'is_featured': True,
                'order': 3
            },
            {
                'name': 'Consultoría Técnica',
                'description': 'Asesoramos en la selección de tecnologías, arquitectura de sistemas y mejores prácticas de desarrollo. Te ayudamos a tomar las decisiones técnicas correctas.',
                'short_description': 'Asesoría en tecnología y arquitectura',
                'icon': 'fas fa-lightbulb',
                'is_featured': False,
                'order': 4
            },
            {
                'name': 'Mantenimiento y Soporte',
                'description': 'Brindamos soporte técnico continuo, mantenimiento preventivo y actualizaciones para tus aplicaciones y sistemas existentes.',
                'short_description': 'Soporte continuo para tus aplicaciones',
                'icon': 'fas fa-tools',
                'is_featured': False,
                'order': 5
            }
        ]
        
        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                name=service_data['name'],
                defaults=service_data
            )
            if created:
                self.stdout.write(f'✓ Servicio creado: {service.name}')
        
        # Create Projects
        projects_data = [
            {
                'name': 'Sistema de Gestión Empresarial',
                'description': 'Desarrollo de un sistema completo de gestión empresarial con módulos de inventario, ventas, contabilidad y recursos humanos. Implementado con Django y React.',
                'short_description': 'Sistema ERP completo con múltiples módulos',
                'technologies': 'Django, React, PostgreSQL, Redis, Celery',
                'status': 'completed',
                'is_featured': True,
                'order': 1
            },
            {
                'name': 'App Móvil de Delivery',
                'description': 'Aplicación móvil para servicio de delivery con geolocalización, pagos en línea y seguimiento en tiempo real. Incluye panel administrativo web.',
                'short_description': 'App de delivery con geolocalización',
                'technologies': 'React Native, Django REST, PostgreSQL, Stripe API',
                'status': 'completed',
                'is_featured': True,
                'order': 2
            },
            {
                'name': 'Portal Educativo Online',
                'description': 'Plataforma de educación online con cursos, evaluaciones, certificaciones y sistema de pagos. Incluye funcionalidades para estudiantes y profesores.',
                'short_description': 'Plataforma de cursos online',
                'technologies': 'Django, Vue.js, PostgreSQL, AWS S3',
                'status': 'in_progress',
                'is_featured': True,
                'order': 3
            },
            {
                'name': 'API de Integraciones Bancarias',
                'description': 'Desarrollo de API REST para integrar múltiples servicios bancarios y procesadores de pago, con documentación completa y SDK.',
                'short_description': 'API para integraciones bancarias',
                'technologies': 'Django REST, PostgreSQL, Redis, Docker',
                'status': 'completed',
                'is_featured': False,
                'order': 4
            }
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                name=project_data['name'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'✓ Proyecto creado: {project.name}')
        
        # Create Team Members
        team_data = [
            {
                'name': 'Carlos Subero',
                'position': 'CEO & Lead Developer',
                'bio': 'Desarrollador full-stack con más de 8 años de experiencia. Especializado en Django, React y arquitecturas escalables. Apasionado por crear soluciones innovadoras.',
                'email': 'carlos@tapara.dev',
                'is_active': True,
                'order': 1
            },
            {
                'name': 'María González',
                'position': 'Frontend Developer',
                'bio': 'Especialista en React, Vue.js y diseño de interfaces. Con experiencia en UX/UI y desarrollo de aplicaciones web modernas y responsivas.',
                'email': 'maria@tapara.dev',
                'is_active': True,
                'order': 2
            },
            {
                'name': 'José Rodríguez',
                'position': 'Mobile Developer',
                'bio': 'Desarrollador móvil especializado en React Native y Flutter. Experiencia en publicación de apps en App Store y Google Play.',
                'email': 'jose@tapara.dev',
                'is_active': True,
                'order': 3
            }
        ]
        
        for member_data in team_data:
            member, created = TeamMember.objects.get_or_create(
                email=member_data['email'],
                defaults=member_data
            )
            if created:
                self.stdout.write(f'✓ Miembro del equipo creado: {member.name}')
        
        self.stdout.write(
            self.style.SUCCESS('✅ Datos de ejemplo creados exitosamente!')
        )