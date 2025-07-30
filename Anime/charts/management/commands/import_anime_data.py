import csv
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from charts.models import Anime

class Command(BaseCommand):
    help = 'Import anime data from CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='data/anime-dataset-2023.csv',
            help='Path to the CSV file relative to the app directory'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing anime data before importing'
        )

    def handle(self, *args, **options):
        csv_file_path = options['file']
        
        # Construct the full path to the CSV file
        if not os.path.isabs(csv_file_path):
            # If it's a relative path, make it relative to the app directory
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            csv_file_path = os.path.join(base_dir, csv_file_path)
        
        if not os.path.exists(csv_file_path):
            raise CommandError(f'CSV file does not exist: {csv_file_path}')

        # Clear existing data if requested
        if options['clear']:
            self.stdout.write('Clearing existing anime data...')
            Anime.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Existing data cleared.'))

        # Import data from CSV
        self.stdout.write(f'Importing data from {csv_file_path}...')
        
        created_count = 0
        updated_count = 0
        error_count = 0

        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row_num, row in enumerate(reader, start=2):  # Start at 2 because row 1 is header
                    try:
                        # Clean and prepare data
                        anime_data = self.clean_row_data(row)
                        
                        # Create or update anime record
                        anime, created = Anime.objects.update_or_create(
                            anime_id=anime_data['anime_id'],
                            defaults=anime_data
                        )
                        
                        if created:
                            created_count += 1
                        else:
                            updated_count += 1
                            
                        if (created_count + updated_count) % 50 == 0:
                            self.stdout.write(f'Processed {created_count + updated_count} records...')
                            
                    except Exception as e:
                        error_count += 1
                        self.stdout.write(
                            self.style.ERROR(f'Error processing row {row_num}: {str(e)}')
                        )
                        continue

        except Exception as e:
            raise CommandError(f'Error reading CSV file: {str(e)}')

        # Display results
        self.stdout.write(
            self.style.SUCCESS(
                f'Import completed successfully!\n'
                f'Created: {created_count} records\n'
                f'Updated: {updated_count} records\n'
                f'Errors: {error_count} records'
            )
        )

    def clean_row_data(self, row):
        """Clean and prepare row data for database insertion"""
        
        def clean_text(text):
            """Clean text fields"""
            if not text or text.strip().lower() in ['unknown', 'nan', '']:
                return None
            return text.strip()

        def clean_number(value, default=0):
            """Clean numeric fields"""
            if not value or str(value).strip().lower() in ['unknown', 'nan', '']:
                return default
            try:
                # Remove commas and convert to int
                return int(str(value).replace(',', '').replace('.0', ''))
            except (ValueError, TypeError):
                return default

        def clean_float(value):
            """Clean float fields"""
            if not value or str(value).strip().lower() in ['unknown', 'nan', '']:
                return None
            try:
                return str(float(value))
            except (ValueError, TypeError):
                return None

        return {
            'anime_id': int(row['anime_id']),
            'name': row['Name'].strip(),
            'english_name': clean_text(row['English name']),
            'other_name': clean_text(row['Other name']),
            'score': clean_float(row['Score']),
            'genres': row['Genres'].strip() if row['Genres'] else '',
            'synopsis': row['Synopsis'].strip() if row['Synopsis'] else '',
            'Type': row['Type'].strip() if row['Type'] else 'Unknown',
            'episodes': clean_text(row['Episodes']) or 'Unknown',
            'aired': row['Aired'].strip() if row['Aired'] else '',
            'premiered': clean_text(row['Premiered']),
            'status': row['Status'].strip() if row['Status'] else 'Unknown',
            'producers': clean_text(row['Producers']),
            'licensors': clean_text(row['Licensors']),
            'studios': clean_text(row['Studios']),
            'source': row['Source'].strip() if row['Source'] else 'Unknown',
            'duration': row['Duration'].strip() if row['Duration'] else 'Unknown',
            'rating': row['Rating'].strip() if row['Rating'] else 'Unknown',
            'rank': clean_text(row['Rank']),
            'popularity': clean_number(row['Popularity']),
            'favorites': clean_number(row['Favorites']),
            'scored_by': clean_text(row['Scored By']) or '0',
            'members': clean_number(row['Members']),
            'image_url': row['Image URL'].strip() if row['Image URL'] else '',
        }
