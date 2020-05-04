TEMPLATES = [{
  'BACKEND': 'django.template.backends.django.DjangoTemplates',
  'DIRS': [
    os.path.join(BASE_DIR, 'templates'),
  ],
  'OPTIONS': {
    'builtins': [
      'audio.templatetags.verbatim'
    ],
  }
}]