import csv
from django.http import HttpResponse


def export_to_csv(data, filename, fieldnames):
    """
    Export data to CSV format.
    
    Args:
        data: List of dictionaries or queryset
        filename: Output filename
        fieldnames: List of field names
    
    Returns:
        HttpResponse with CSV file
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    writer = csv.DictWriter(response, fieldnames=fieldnames)
    writer.writeheader()
    
    for item in data:
        if hasattr(item, '__dict__'):
            row = {field: getattr(item, field, '') for field in fieldnames}
        else:
            row = item
        writer.writerow(row)
    
    return response
