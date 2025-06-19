from django.shortcuts import render

def home(request):
    context = {
        'hero_title': 'Find your way to gain an edge in steel turning',
        'hero_subtitle': 'Dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua minim.',
        'services': [
            {
                'title': 'Quality control',
                'number': '01',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
            },
            {
                'title': 'Unique equipment',
                'number': '02',
                'description': 'Sed do eiusmod tempor incididunt ut labore et dolore magna.'
            }
        ],
        'testimonials': [
            {
                'name': 'Kevin Rogers',
                'text': 'Integer consectetur arcu a purus dignissim elementum. Aenean quis urna non eros suscipit pretium cursus non ipsum.',
                'image': 'testimonial-1.jpg'
            },
            {
                'name': 'Peter Parker',
                'text': 'Integer consectetur arcu a purus dignissim elementum. Aenean quis urna non eros suscipit pretium cursus non ipsum.',
                'image': 'testimonial-2.jpg'
            },
            {
                'name': 'Jason Bright',
                'text': 'Integer consectetur arcu a purus dignissim elementum. Aenean quis urna non eros suscipit pretium cursus non ipsum.',
                'image': 'testimonial-3.jpg'
            }
        ]
    }
    return render(request, 'home.html', context)